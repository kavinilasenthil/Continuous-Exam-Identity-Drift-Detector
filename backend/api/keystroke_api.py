from flask import Flask, request, jsonify
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'features'))
from keystroke_features import extract_keystroke_features

app = Flask(__name__)

@app.route('/keystroke-score', methods=['POST'])
def keystroke_score():
    file = request.files['file']
    file.save('temp_keystrokes.csv')
    result = extract_keystroke_features('temp_keystrokes.csv')
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5001, debug=True)