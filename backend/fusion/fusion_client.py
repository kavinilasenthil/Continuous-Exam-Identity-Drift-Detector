import requests

def get_keystroke_score(csv_path):
    """Calls Member 1's keystroke endpoint with a CSV file."""
    response = requests.post(
        'http://127.0.0.1:5001/keystroke-score',
        files={'file': open(csv_path, 'rb')}
    )
    return response.json()


def get_mouse_score(csv_path):
    """Calls Member 2's mouse endpoint with a CSV file."""
    response = requests.post(
        'http://127.0.0.1:5002/mouse-score',
        files={'file': open(csv_path, 'rb')}
    )
    return response.json()


def get_stylometry_score(text):
    """Calls Member 3's stylometry endpoint with JSON text (not a file)."""
    response = requests.post(
        'http://127.0.0.1:5003/stylometry-score',
        json={'text': text}
    )
    return response.json()