from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  # renamed from location.html

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    print("📍 Received location:", data)

    # Save to file
    with open("location.txt", "a") as f:
        f.write(f"{data['latitude']}, {data['longitude']}\n")

    return jsonify({"status": "received"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render uses dynamic ports
    app.run(host='0.0.0.0', port=port)
