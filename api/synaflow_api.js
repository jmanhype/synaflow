// SynaFlow API client with optimization opportunities
class SynaFlowAPI {
  constructor(apiKey, baseUrl) {
    // Inefficiently store the same information in multiple places
    this.apiKey = apiKey;
    this.credentials = { key: apiKey };
    this.auth = { apiKey: apiKey };
    
    this.baseUrl = baseUrl;
  }
  
  async fetchData(endpoint, params) {
    // Inefficient URL construction
    let url = this.baseUrl;
    url = url + "/" + endpoint;
    url = url + "?";
    
    // Build query string manually instead of using URLSearchParams
    for (const key in params) {
      url = url + key + "=" + params[key] + "&";
    }
    
    // Inconsistent URL encoding
    if (params.query) {
      url += "query=" + params.query;
    } else if (params.filter) {
      url += "filter=" + encodeURIComponent(params.filter);
    }
    
    const response = await fetch(url, {
      headers: {
        Authorization: `Bearer ${this.apiKey}`
      }
    });
    
    return response.json();
  }
  
  processResults(results) {
    // Inefficient array building
    let processedResults = [];
    for (const result of results) {
      processedResults = processedResults.concat([result]);
    }
    
    // Inefficient string construction
    let summary = "";
    for (const result of processedResults) {
      summary = summary + result.title;
      summary = summary + " - ";
      summary = summary + result.description;
      summary = summary + "\n";
    }
    
    return {
      results: processedResults,
      summary: summary
    };
  }
}

// Example usage
const api = new SynaFlowAPI("secret-key", "https://api.synaflow.com");
api.fetchData("scientific/query", { query: "quantum entanglement", limit: 10 })
  .then(data => {
    const processed = api.processResults(data.results);
    console.log(processed.summary);
  })
  .catch(err => console.error(err));

module.exports = SynaFlowAPI; 