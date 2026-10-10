# Runs at http://127.0.0.1:5003/stylometry-score — expects JSON body: {"text": "..."}
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'features'))

from flask import Flask, request, jsonify
from stylometry_features import extract_stylometry_features

app = Flask(__name__)


@app.route('/stylometry-score', methods=['POST'])
def stylometry_score():
    try:
        data = request.get_json(silent=True)
        if data is None or 'text' not in data:
            return jsonify({'error': "Request body must be JSON containing a 'text' key"}), 400

        text = data['text']
        if not isinstance(text, str) or not text.strip():
            return jsonify({'error': "'text' must be a non-empty string"}), 400

        result = extract_stylometry_features(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(port=5003, debug=True)