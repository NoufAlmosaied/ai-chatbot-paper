from flask import Flask, request, jsonify, render_template
from services.ml_service import MLService
from services.feature_extractor import FeatureExtractor
from services.html_fetcher import HTMLFetcher
from chatbot.conversation import ConversationManager
from chatbot.risk_analyzer import RiskAnalyzer
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

feature_extractor = FeatureExtractor()
html_fetcher = HTMLFetcher()
conversation_manager = ConversationManager()
risk_analyzer = RiskAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')
    session_id = data.get('session_id', 'default')
    
    response = conversation_manager.process_message(session_id, message)
    return jsonify(response)

@app.route('/api/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url', '')
    
    features = feature_extractor.extract_url_features(url)
    html_content = html_fetcher.fetch(url)
    
    return jsonify({
        "url": url,
        "features": features,
        "status": "analyzed"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
