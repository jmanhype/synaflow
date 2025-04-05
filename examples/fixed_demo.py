import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from src.simplified_program import SimplifiedScientificQA

def main():
    print("Welcome to SynaFlow Scientific QA Demo")
    print("--------------------------------------")
    
    # Initialize the QA system
    qa_system = SimplifiedScientificQA()
    
    while True:
        # Get user input
        question = input("\nEnter a scientific question (or 'exit' to quit): ")
        
        if question.lower() in ['exit', 'quit', 'q']:
            print("Thank you for using SynaFlow!")
            break
        
        # Process the question
        try:
            print("\nProcessing your question...")
            answer = qa_system.answer_question(question)
            
            # Display the answer
            print("\nAnswer:")
            print(answer)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("There was an error processing your question. Please try again.")

if __name__ == "__main__":
    main()
