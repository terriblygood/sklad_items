from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        "service": "service1",
        "status": "healthy",
        "port": os.getenv("PORT", 5001)
    })

@app.route('/data')
def get_data():
    return jsonify({
        "service": "service1",
        "message": "Hello from Service 1!",
        "data": ["item1", "item2", "item3"]
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
