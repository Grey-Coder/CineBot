from flask import Flask, request, send_from_directory, jsonify
import requests

app = Flask(__name__, static_folder='static')

# URL where Rasa server is running locally
RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'

# Serve the static HTML UI from a folder named "static"
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Proxy API requests to the Rasa server
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    # Forward the message to the Rasa server
    try:
        response = requests.post(RASA_URL, json=data)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run Flask server on port 8080 (or any port you choose)
    app.run(host='0.0.0.0', port=8080, debug=True)
