# SynaFlow Responsive GUI Documentation

## Overview

This documentation covers the responsive GUI implementation added to the SynaFlow scientific question answering system. The GUI provides an intuitive interface for users to interact with the system across desktop, tablet, and mobile devices.

## Implementation Details

### Directory Structure

```
synaflow/
├── static/               # Static files for the GUI
│   ├── css/              # CSS stylesheets
│   │   └── styles.css    # Main stylesheet
│   ├── js/               # JavaScript files
│   │   └── app.js        # Frontend logic and API integration
│   └── index.html        # Main HTML file
├── api/
│   └── app.py            # FastAPI backend serving the GUI and API
```

### Technologies Used

- **Frontend**:
  - HTML5
  - CSS3 with responsive design
  - JavaScript (ES6+)
  - Bootstrap 5 for layout and components

- **Backend**:
  - FastAPI for API endpoints and serving static files
  - Python 3.10+ for backend logic
  - SynaLinks for scientific question answering

## Features

1. **Responsive Design**
   - Adapts to desktop, tablet, and mobile screen sizes
   - Touch-friendly controls for mobile users
   - Collapsible sections for better mobile experience

2. **Question Input Interface**
   - Text input for scientific questions
   - Domain selection dropdown (physics, biology, etc.)
   - Optional context input area

3. **Answer Display**
   - Structured sections for background, reasoning, and answer
   - Visual confidence indicator
   - Citations with source information
   - Further reading recommendations

4. **History Management**
   - Saves question history locally
   - Allows revisiting previous questions and answers
   - Option to clear history

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jmanhype/synaflow.git
   cd synaflow
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the Application**
   ```bash
   python api/app.py
   ```

5. **Access the GUI**
   - Open a browser and navigate to `http://localhost:8000`

## Usage Guide

### Asking a Scientific Question

1. Enter your scientific question in the text area
2. Optionally select a domain from the dropdown menu
3. Optionally provide additional context
4. Click "Submit Question"
5. Wait for the system to process your question
6. View the structured answer with citations

### Viewing Question History

1. Previous questions appear in the sidebar
2. Click on any previous question to view its answer again
3. Use the "Clear History" button to remove all history

### Mobile Usage Tips

- Use landscape orientation for better viewing of answer sections
- Tap section headers to focus on specific parts of the answer
- Scroll horizontally on citation items if needed

## API Integration

The frontend communicates with the backend through a REST API:

- **Endpoint**: `/api/query`
- **Method**: POST
- **Request Format**:
  ```json
  {
    "question": "What is quantum entanglement?",
    "domain": "physics",
    "context": "I'm a university student"
  }
  ```
- **Response Format**:
  ```json
  {
    "request_id": "req-1234567890abcdef",
    "timestamp": 1617123456.789,
    "result": {
      "background": "...",
      "reasoning": "...",
      "answer": "...",
      "confidence": 0.95,
      "citations": [...],
      "further_reading": [...]
    }
  }
  ```

## Customization

### Changing Colors and Styling

The color scheme and styling can be customized by editing the CSS variables in `static/css/styles.css`:

```css
:root {
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --accent-color: #e74c3c;
    --light-bg: #f8f9fa;
    --dark-bg: #343a40;
    --text-color: #333;
    --light-text: #f8f9fa;
}
```

### Adding New Domains

To add new domains to the dropdown menu, edit the options in `static/index.html`:

```html
<select class="form-select" id="domain">
    <option value="">Select a domain</option>
    <option value="physics">Physics</option>
    <!-- Add new domains here -->
</select>
```

## Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Check that the backend server is running
   - Verify API endpoint URL in `app.js`
   - Check browser console for error messages

2. **Display Issues on Mobile**
   - Ensure viewport meta tag is present in HTML
   - Test on different devices and browsers
   - Check for CSS conflicts

3. **Question Processing Errors**
   - Verify OpenAI API key is valid
   - Check server logs for backend errors
   - Ensure question format is valid

## Future Enhancements

1. **User Authentication**
   - Add login/registration functionality
   - Save question history to user accounts
   - Personalized experience based on user preferences

2. **Advanced Visualization**
   - Add charts and graphs for scientific data
   - Interactive models for complex concepts
   - LaTeX support for mathematical equations

3. **Offline Support**
   - Progressive Web App (PWA) capabilities
   - Offline access to previously fetched answers
   - Background synchronization for new questions

## Credits

- SynaFlow core functionality by jmanhype
- Responsive GUI implementation added as an enhancement
- Built with SynaLinks framework
