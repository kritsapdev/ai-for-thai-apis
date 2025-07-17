from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# Load API2_URL from environment variable
API2_URL = os.getenv('API2_URL', 'http://api2:5001/analyze') 
# AI for Thai API Key for Summarization
AIFORTHAI_SUMMARIZE_API_KEY = os.getenv('AIFORTHAI_SUMMARIZE_API_KEY', 'YOUR_AIFORTHAI_SUMMARIZE_API_KEY') 

@app.route('/summarize', methods=['POST'])
def summarize_text():
    print("--- API1: Received request ---")
    
    data = request.json
    if not data or 'text' not in data:
        print("--- API1: Invalid request, 'text' field missing ---")
        return jsonify({"error": "Missing 'text' field in request"}), 400

    original_text = data['text']
    print(f"--- API1: Original text received: {original_text[:50]}... ---") # Print first 50 chars

    # Prepare data for AI for Thai Summarization API
    summarize_payload = json.dumps([{"id": 100, "comp_rate": 30, "src": original_text}])
    summarize_url = 'https://api.aiforthai.in.th/textsummarize'
    summarize_headers = {
        'Apikey': AIFORTHAI_SUMMARIZE_API_KEY, 
        'Content-Type': 'application/json'
    }

    try:
        print("--- API1: Sending request to AI for Thai Summarization API ---")
        summarize_response = requests.post(summarize_url, data=summarize_payload, headers=summarize_headers)
        summarize_response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        summarized_data = summarize_response.json()
        print(f"--- API1: Received response from AI for Thai Summarization: {summarized_data} ---")
        
        # Extract summarized text
        summarized_text = ""
        if summarized_data and isinstance(summarized_data, list) and len(summarized_data) > 0:
            summarized_text = summarized_data[0].get('text', '')

        print(f"--- API1: Summarized text: {summarized_text[:50]}... ---")

        # Now, send the summarized text to API2 for sentiment analysis
        print(f"--- API1: Forwarding summarized text to API2 at {API2_URL} ---")
        api2_response = requests.post(API2_URL, json={'text': summarized_text})
        api2_response.raise_for_status()
        sentiment_data = api2_response.json()
        print(f"--- API1: Received response from API2: {sentiment_data} ---")

        final_response = {
            "original_text": original_text,
            "summarized_text": summarized_text,
            "sentiment_analysis": sentiment_data
        }
        print("--- API1: Sending final response back to user ---")
        return jsonify(final_response)

    except requests.exceptions.RequestException as e:
        print(f"--- API1: Error during API call: {e} ---")
        return jsonify({"error": f"Failed to connect to AI for Thai or API2: {e}"}), 500
    except json.JSONDecodeError:
        print("--- API1: Error decoding JSON from AI for Thai ---")
        return jsonify({"error": "Failed to decode JSON from AI for Thai API"}), 500
    except Exception as e:
        print(f"--- API1: An unexpected error occurred: {e} ---")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"--- API1: Starting on port {port} ---")
    app.run(host='0.0.0.0', port=port, debug=False) # debug=False for production