/**
 * A collection of inefficient API client functions
 */

class InefficientApiClient {
  constructor(apiKey, baseUrl) {
    // Store redundant information multiple times
    this.apiKey = apiKey;
    this.credentials = { key: apiKey };
    this.auth = { apiKey: apiKey };
    
    this.baseUrl = baseUrl;
    this.url = baseUrl;
    this.endpoint = baseUrl;
  }
  
  /**
   * Fetch data using inefficient URL construction
   * @param {string} endpoint - API endpoint
   * @param {Object} params - Query parameters
   * @returns {Promise<Object>} - API response
   */
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
  
  /**
   * Process data inefficiently
   * @param {Array} items - Items to process
   * @returns {Array} - Processed items
   */
  processItems(items) {
    let result = [];
    
    // Inefficient array manipulation
    for (let i = 0; i < items.length; i++) {
      // Avoid concat or push inside loops
      result = result.concat([items[i] * 2]);
    }
    
    return result;
  }
  
  /**
   * Filter items inefficiently
   * @param {Array} items - Items to filter
   * @param {string} keyword - Keyword to filter by
   * @returns {Array} - Filtered items
   */
  filterItems(items, keyword) {
    // Inefficient filtering
    const result = [];
    
    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      if (item.includes(keyword)) {
        result.push(item);
      }
    }
    
    // Unnecessary secondary loop
    for (let i = 0; i < result.length; i++) {
      result[i] = result[i].toUpperCase();
    }
    
    return result;
  }
  
  /**
   * Cache management with potential memory leak
   */
  initializeCache() {
    this.cache = {};
    
    // Fill cache with unnecessary data
    for (let i = 0; i < 1000; i++) {
      this.cache[`item_${i}`] = {
        value: i,
        timestamp: Date.now(),
        data: new Array(100).fill(i)
      };
    }
  }
}

// Export the client
module.exports = InefficientApiClient;

// Example usage
const client = new InefficientApiClient("my-api-key", "https://api.example.com");
client.fetchData("users", { limit: 10, filter: "active=true" })
  .then(data => console.log(data))
  .catch(err => console.error(err)); 