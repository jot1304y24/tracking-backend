from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging

app = Flask(__name__)
CORS(app, origins=["https://keen-bublanina-0e9b3c.netlify.app"])
logging.basicConfig(level=logging.DEBUG)

@app.route('/location', methods=['POST'])
def get_location():
    logging.debug("Received a request to /location")
    try:
        data = request.get_json()
        logging.debug(f"Received data: {data}")
        print("📍 Received location:", data)

        # Save to file
        with open("location.txt", "a") as f:
            f.write(f"{data['latitude']}, {data['longitude']}\\n")

        return jsonify({"status": "received"})
    except Exception as e:
        logging.error(f"Error processing location: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
