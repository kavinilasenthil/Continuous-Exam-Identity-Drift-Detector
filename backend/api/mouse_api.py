# Runs at http://127.0.0.1:5002/mouse-score
from flask import Flask, request, jsonify
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'features'))
from mouse_features import extract_mouse_features

app = Flask(__name__)


@app.route('/mouse-score', methods=['POST'])
def mouse_score():
    try:
        file = request.files['file']
        file.save('temp_mouse.csv')
        result = extract_mouse_features('temp_mouse.csv')
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': 'Could not process mouse file: ' + str(e)}), 400


if __name__ == '__main__':
    app.run(port=5002, debug=True)
