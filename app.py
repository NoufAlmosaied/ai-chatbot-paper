from flask import Flask, request, jsonify, render_template
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
