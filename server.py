from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/location', methods=['POST'])
def get_location():
    data = request.get_json()  # Use get_json()
    print("📍 Received location:", data)

    # Save to file
    with open("location.txt", "a") as f:
        f.write(f"{data['latitude']}, {data['longitude']}\\n")

    return jsonify({"status": "received"})

@app.route('/locations', methods=['GET'])  # New endpoint to get locations
def get_locations():
    try:
        with open("location.txt", "r") as f:
            locations = f.readlines()
        # Format the data for better readability
        locations = [loc.strip().split(', ') for loc in locations]
        return jsonify({"locations": locations})
    except FileNotFoundError:
        return jsonify({"error": "No location data found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
