"""
Fusion Engine v1 — combines REAL keystroke, mouse, and stylometry feature
dictionaries (returned live from teammates' Flask endpoints) into one score.
"""

TYPING_SPEED_REF = 4.5
MOUSE_SPEED_REF = 250
FLESCH_REF = 55


def combine_scores(keystroke_features, mouse_features, stylometry_features):
    typing_speed = keystroke_features.get('typing_speed')
    avg_speed = mouse_features.get('avg_speed')
    flesch = stylometry_features.get('Flesch Reading Ease')  # matches Member 3's actual key

    if typing_speed is None or avg_speed is None or flesch is None:
        raise KeyError("Missing expected key in one of the input feature dictionaries")

    norm_typing = typing_speed / TYPING_SPEED_REF
    norm_mouse = avg_speed / MOUSE_SPEED_REF
    norm_flesch = flesch / FLESCH_REF

    fusion_score = (norm_typing + norm_mouse + norm_flesch) / 3
    return fusion_score


if __name__ == '__main__':
    from fusion_client import get_keystroke_score, get_mouse_score, get_stylometry_score

    keystroke = get_keystroke_score('sample_keystrokes.csv')
    mouse = get_mouse_score('sample_mouse.csv')
    stylometry = get_stylometry_score("This is a sample answer paragraph for testing.")

    print("Keystroke:", keystroke)
    print("Mouse:", mouse)
    print("Stylometry:", stylometry)

    score = combine_scores(keystroke, mouse, stylometry)
    print("Fusion score:", score)