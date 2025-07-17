from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# AI for Thai API Key for Social Sensing (SSENSE)
AIFORTHAI_SSENSE_API_KEY = os.getenv('AIFORTHAI_SSENSE_API_KEY', 'YOUR_AIFORTHAI_SSENSE_API_KEY') 

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    print("--- API2: Received request ---")
    
    data = request.json
    if not data or 'text' not in data:
        print("--- API2: Invalid request, 'text' field missing ---")
        return jsonify({"error": "Missing 'text' field in request"}), 400

    text_to_analyze = data['text']
    print(f"--- API2: Text received for analysis: {text_to_analyze[:50]}... ---") # Print first 50 chars

    # Prepare data for AI for Thai Social Sensing API
    ssense_url = "https://api.aiforthai.in.th/ssense"
    ssense_data = {'text': text_to_analyze}
    ssense_headers = {
        'Apikey': AIFORTHAI_SSENSE_API_KEY
    }

    try:
        print("--- API2: Sending request to AI for Thai Social Sensing API ---")
        ssense_response = requests.post(ssense_url, data=ssense_data, headers=ssense_headers)
        ssense_response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        sentiment_result = ssense_response.json()
        print(f"--- API2: Received response from AI for Thai Social Sensing: {sentiment_result} ---")
        print("--- API2: Sending response back to API1 ---")
        return jsonify(sentiment_result)

    except requests.exceptions.RequestException as e:
        print(f"--- API2: Error during API call to AI for Thai: {e} ---")
        return jsonify({"error": f"Failed to connect to AI for Thai SSENSE API: {e}"}), 500
    except json.JSONDecodeError:
        print("--- API2: Error decoding JSON from AI for Thai SSENSE API ---")
        return jsonify({"error": "Failed to decode JSON from AI for Thai SSENSE API"}), 500
    except Exception as e:
        print(f"--- API2: An unexpected error occurred: {e} ---")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    print(f"--- API2: Starting on port {port} ---")
    app.run(host='0.0.0.0', port=port, debug=False) # debug=False for production