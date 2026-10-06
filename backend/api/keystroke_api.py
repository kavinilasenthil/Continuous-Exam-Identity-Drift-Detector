# Runs at http://127.0.0.1:5001/keystroke-score
import os
import sys
import tempfile
import traceback

from flask import Flask, request, jsonify

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'features'))
from keystroke_features import extract_keystroke_features

app = Flask(__name__)


@app.route('/keystroke-score', methods=['POST'])
def keystroke_score():
    tmp_path = None
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded. Send a CSV in the "file" field.'}), 400

        file = request.files['file']

        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp:
            file.save(tmp.name)
            tmp_path = tmp.name

        features = extract_keystroke_features(tmp_path)

        return jsonify(features)

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': f'Could not process request: {str(e)}'}), 400

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)


if __name__ == '__main__':
    app.run(port=5001, debug=True)