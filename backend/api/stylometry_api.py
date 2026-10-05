import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'features'))

from flask import Flask, request, jsonify
from stylometry_features import extract_stylometry_features

app = Flask(__name__)


@app.route('/stylometry-score', methods=['POST'])
def stylometry_score():
    data = request.get_json()
    text = data['text']
    result = extract_stylometry_features(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5003, debug=True)