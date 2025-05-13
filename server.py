from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import logging

app = Flask(__name__)
CORS(app, origins=["https://keen-bublanina-0e9b3c.netlify.app"])  # Add CORS for Netlify
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/location', methods=['POST'])
def get_location():
    logging.debug("Received a request to /location")
    try:
        data = request.get_json()  # Use get_json() to parse JSON
        logging.debug(f"Received data: {data}")
        print("📍 Received location:", data)

        # Save to file
        with open("location.txt", "a") as f:
            f.write(f"{data['latitude']}, {data['longitude']}\\n")

        return jsonify({"status": "received"})
    except Exception as e:
        logging.error(f"Error processing location: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500  # Return error status code

@app.route('/locations', methods=['GET'])
def get_locations():
    logging.debug("Received a request to /locations")
    try:
        with open("location.txt", "r") as f:
            locations = f.readlines()
        # Format the data for better readability
        locations = [loc.strip().split(', ') for loc in locations]
        return jsonify({"locations": locations})
    except FileNotFoundError:
        logging.error("Error: location.txt not found")
        return jsonify({"error": "No location data found"}), 404  # Return 404 for not found

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
