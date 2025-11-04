from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import json
import asyncio
from typing import Dict, Any, Optional

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the SimplifiedScientificQA class
try:
    from src.simplified_program import SimplifiedScientificQA
except ImportError:
    print("Error importing SimplifiedScientificQA. Make sure the path is correct.")
    # Create a mock class for testing if import fails
    class SimplifiedScientificQA:
        async def __call__(self, query: Dict[str, Any]) -> Dict[str, Any]:
            return {
                "background": "This is a mock background response.",
                "reasoning": "This is mock reasoning since the actual model couldn't be loaded.",
                "answer": f"Mock answer to: {query.get('question', 'unknown question')}",
                "confidence": 0.7,
                "citations": [
                    {
                        "title": "Mock Citation",
                        "authors": ["Author 1", "Author 2"],
                        "year": 2023,
                        "source": "Mock Journal",
                        "url": "https://example.com/mock"
                    }
                ],
                "further_reading": ["Mock Reading 1", "Mock Reading 2"]
            }

# Create FastAPI app
app = FastAPI(title="SynaFlow API", description="Scientific Question Answering API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the QA system
qa_system = None

@app.on_event("startup")
async def startup_event():
    global qa_system
    try:
        # Try to load from a trained model file if available
        model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                 "models", "trained_qa_program.json")
        if os.path.exists(model_path):
            qa_system = SimplifiedScientificQA.from_file(model_path)
            print(f"Loaded QA system from {model_path}")
        else:
            # Initialize with default settings
            qa_system = SimplifiedScientificQA()
            print("Initialized default QA system")
    except Exception as e:
        print(f"Error initializing QA system: {e}")
        qa_system = SimplifiedScientificQA()  # Fallback to default

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "SynaFlow API"}

@app.post("/api/query")
async def query(request: Request):
    try:
        # Parse the request body
        try:
            data = await request.json()
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON in request body")

        # Extract query parameters
        question = data.get("question")
        domain = data.get("domain")
        context = data.get("context")

        if not question:
            raise HTTPException(status_code=400, detail="Question is required")

        if not isinstance(question, str) or len(question.strip()) == 0:
            raise HTTPException(status_code=400, detail="Question must be a non-empty string")

        # Validate question length
        if len(question) > 1000:
            raise HTTPException(status_code=400, detail="Question too long (max 1000 characters)")

        # Create query object
        query_obj = {
            "question": question.strip(),
            "domain": domain,
            "context": context
        }

        # Process the query
        if qa_system is None:
            raise HTTPException(status_code=503, detail="QA system not initialized. Please try again later.")

        try:
            result = await asyncio.wait_for(qa_system(query_obj), timeout=30.0)
        except asyncio.TimeoutError:
            raise HTTPException(status_code=504, detail="Query processing timeout. Please try a simpler question.")

        # Return the response
        return {
            "request_id": "req-" + os.urandom(8).hex(),
            "timestamp": asyncio.get_event_loop().time(),
            "result": result
        }
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html for the root path
@app.get("/")
async def read_root():
    try:
        static_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static", "index.html")
        with open(static_path, "r") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Frontend not found. Please ensure static/index.html exists.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
