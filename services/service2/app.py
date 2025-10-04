from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        "service": "service2",
        "status": "healthy",
        "port": os.getenv("PORT", 5002)
    })

@app.route('/info')
def get_info():
    return jsonify({
        "service": "service2",
        "message": "Hello from Service 2!",
        "configuration": {
            "environment": "development",
            "version": "1.0.0"
        }
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5002))
    app.run(host='0.0.0.0', port=port, debug=True)
