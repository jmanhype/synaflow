// app.js - Backend integration for SynaFlow GUI
const API_ENDPOINT = '/api/query';

document.addEventListener('DOMContentLoaded', function() {
    const questionForm = document.getElementById('questionForm');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const answerContainer = document.getElementById('answerContainer');
    const historyList = document.getElementById('historyList');
    
    // Store question history
    let questionHistory = [];
    
    // Load history from localStorage if available
    if (localStorage.getItem('synaflowHistory')) {
        try {
            questionHistory = JSON.parse(localStorage.getItem('synaflowHistory'));
            updateHistory();
        } catch (e) {
            console.error('Error loading history:', e);
            localStorage.removeItem('synaflowHistory');
        }
    }
    
    // Form submission handler
    questionForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form values
        const question = document.getElementById('question').value;
        const domain = document.getElementById('domain').value;
        const context = document.getElementById('context').value;
        
        if (!question.trim()) {
            alert('Please enter a question');
            return;
        }
        
        // Show loading spinner
        loadingSpinner.style.display = 'block';
        answerContainer.style.display = 'none';
        
        try {
            // Prepare request data
            const requestData = {
                question: question,
                domain: domain || undefined,
                context: context || undefined
            };
            
            // Make API call
            const response = await fetch(API_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });
            
            if (!response.ok) {
                throw new Error(`API error: ${response.status}`);
            }
            
            const data = await response.json();
            
            // Process the response
            processResponse({
                question: question,
                domain: domain,
                context: context,
                result: data.result
            });
        } catch (error) {
            console.error('Error:', error);
            loadingSpinner.style.display = 'none';
            
            // Show error message
            answerContainer.style.display = 'block';
            document.getElementById('backgroundText').textContent = 'Error processing your question.';
            document.getElementById('reasoningText').textContent = `An error occurred: ${error.message}`;
            document.getElementById('answerText').textContent = 'Please try again later or contact support if the problem persists.';
            document.getElementById('confidenceBar').style.width = '0%';
            document.getElementById('confidenceText').textContent = '0% confidence';
            document.getElementById('citationsList').innerHTML = '<p class="text-muted">No citations available.</p>';
            document.getElementById('furtherReadingList').innerHTML = '<p class="text-muted">No further reading suggestions available.</p>';
        }
    });
    
    // Process and display the response
    function processResponse(data) {
        // Add to history
        questionHistory.unshift(data);
        
        // Limit history to 10 items
        if (questionHistory.length > 10) {
            questionHistory = questionHistory.slice(0, 10);
        }
        
        // Save to localStorage
        try {
            localStorage.setItem('synaflowHistory', JSON.stringify(questionHistory));
        } catch (e) {
            console.error('Error saving history:', e);
        }
        
        updateHistory();
        
        // Display answer
        document.getElementById('backgroundText').textContent = data.result.background;
        document.getElementById('reasoningText').textContent = data.result.reasoning;
        document.getElementById('answerText').textContent = data.result.answer;
        
        // Update confidence
        const confidenceBar = document.getElementById('confidenceBar');
        const confidenceText = document.getElementById('confidenceText');
        const confidence = data.result.confidence * 100;
        confidenceBar.style.width = confidence + '%';
        confidenceText.textContent = `${confidence.toFixed(1)}% confidence`;
        
        // Update citations
        const citationsList = document.getElementById('citationsList');
        citationsList.innerHTML = '';
        
        if (!data.result.citations || data.result.citations.length === 0) {
            citationsList.innerHTML = '<p class="text-muted">No citations available.</p>';
        } else {
            data.result.citations.forEach(citation => {
                const citationItem = document.createElement('div');
                citationItem.className = 'citation-item';
                
                const title = document.createElement('div');
                title.className = 'citation-title';
                title.textContent = citation.title;
                
                const authors = document.createElement('div');
                authors.className = 'citation-authors';
                authors.textContent = Array.isArray(citation.authors) ? citation.authors.join(', ') : citation.authors;
                
                const details = document.createElement('div');
                details.textContent = `${citation.source} (${citation.year})`;
                
                citationItem.appendChild(title);
                citationItem.appendChild(authors);
                citationItem.appendChild(details);
                
                if (citation.url) {
                    const link = document.createElement('a');
                    link.href = citation.url;
                    link.textContent = 'View Source';
                    link.className = 'btn btn-sm btn-outline-primary mt-2';
                    link.target = '_blank';
                    citationItem.appendChild(link);
                }
                
                citationsList.appendChild(citationItem);
            });
        }
        
        // Update further reading
        const furtherReadingList = document.getElementById('furtherReadingList');
        furtherReadingList.innerHTML = '';
        
        if (!data.result.further_reading || data.result.further_reading.length === 0) {
            furtherReadingList.innerHTML = '<p class="text-muted">No further reading suggestions available.</p>';
        } else {
            data.result.further_reading.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = item;
                furtherReadingList.appendChild(listItem);
            });
        }
        
        // Hide loading spinner and show answer container
        loadingSpinner.style.display = 'none';
        answerContainer.style.display = 'block';
        
        // Scroll to answer
        answerContainer.scrollIntoView({ behavior: 'smooth' });
    }
    
    // Update history list
    function updateHistory() {
        historyList.innerHTML = '';
        
        if (questionHistory.length === 0) {
            historyList.innerHTML = '<p class="text-muted">No questions asked yet.</p>';
        } else {
            questionHistory.forEach((item, index) => {
                const historyItem = document.createElement('div');
                historyItem.className = 'history-item';
                historyItem.dataset.index = index;
                
                const question = document.createElement('div');
                question.className = 'history-question';
                question.textContent = item.question;
                
                historyItem.appendChild(question);
                
                if (item.domain) {
                    const domain = document.createElement('div');
                    domain.className = 'history-domain';
                    domain.textContent = `Domain: ${item.domain}`;
                    historyItem.appendChild(domain);
                }
                
                historyItem.addEventListener('click', function() {
                    const index = parseInt(this.dataset.index);
                    processResponse(questionHistory[index]);
                });
                
                historyList.appendChild(historyItem);
            });
        }
    }
    
    // Clear history button
    const clearHistoryBtn = document.createElement('button');
    clearHistoryBtn.className = 'btn btn-sm btn-outline-danger mt-3';
    clearHistoryBtn.textContent = 'Clear History';
    clearHistoryBtn.addEventListener('click', function() {
        if (confirm('Are you sure you want to clear your question history?')) {
            questionHistory = [];
            localStorage.removeItem('synaflowHistory');
            updateHistory();
        }
    });
    
    historyList.parentNode.appendChild(clearHistoryBtn);
});
