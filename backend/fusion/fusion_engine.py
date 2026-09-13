"""
Fusion Engine Prototype — combines dummy keystroke, mouse, and stylometry
features into a single fusion score.

Feature picked from each module and why:
- keystroke: typing_speed  -> most directly reflects behavioral rhythm changes
- mouse: avg_speed         -> most sensitive single indicator of motor behavior drift
- stylometry: flesch_reading_ease -> most stable, easily comparable readability metric

Reference values below are rough "typical normal" baselines I chose so that
a value close to the reference normalizes to ~1.0 (normal), and values far
above/below it push the fusion score away from 1.0.
"""

# Reference ("normal baseline") values — chosen based on typical ranges
TYPING_SPEED_REF = 4.5          # keys/sec, typical average typing speed
MOUSE_SPEED_REF = 250           # px/sec, typical average mouse speed
FLESCH_REF = 55                 # typical Flesch reading ease score


def combine_scores(keystroke_features, mouse_features, stylometry_features):
    # Pick one representative number from each dictionary
    typing_speed = keystroke_features.get('typing_speed', 0)
    avg_speed = mouse_features.get('avg_speed', 0)
    flesch = stylometry_features.get('flesch_reading_ease', 0)

    # Normalize each by dividing by its reference value
    norm_typing = typing_speed / TYPING_SPEED_REF
    norm_mouse = avg_speed / MOUSE_SPEED_REF
    norm_flesch = flesch / FLESCH_REF

    # Average the three normalized numbers into one fusion score
    fusion_score = (norm_typing + norm_mouse + norm_flesch) / 3

    print(f"Normalized typing speed: {norm_typing:.3f}")
    print(f"Normalized mouse speed: {norm_mouse:.3f}")
    print(f"Normalized Flesch score: {norm_flesch:.3f}")
    print(f"Fusion score: {fusion_score:.3f}")

    return fusion_score


if __name__ == '__main__':
    # Scenario 1: clearly normal behavior
    keystroke_normal = {'avg_dwell_time': 90, 'avg_flight_time': 120, 'typing_speed': 4.2}
    mouse_normal = {'avg_speed': 250, 'click_count': 12, 'avg_click_gap': 1.4, 'path_straightness': 0.7}
    stylometry_normal = {'avg_sentence_length': 18, 'avg_word_length': 4.3, 'flesch_reading_ease': 55, 'function_word_pct': 48}

    # Scenario 2: clearly drifted behavior (very different numbers)
    keystroke_drifted = {'avg_dwell_time': 200, 'avg_flight_time': 300, 'typing_speed': 1.5}
    mouse_drifted = {'avg_speed': 80, 'click_count': 3, 'avg_click_gap': 4.0, 'path_straightness': 0.3}
    stylometry_drifted = {'avg_sentence_length': 9, 'avg_word_length': 6.5, 'flesch_reading_ease': 20, 'function_word_pct': 25}

    # Scenario 3: borderline case
    keystroke_borderline = {'avg_dwell_time': 130, 'avg_flight_time': 180, 'typing_speed': 3.0}
    mouse_borderline = {'avg_speed': 180, 'click_count': 8, 'avg_click_gap': 2.0, 'path_straightness': 0.5}
    stylometry_borderline = {'avg_sentence_length': 14, 'avg_word_length': 5.0, 'flesch_reading_ease': 40, 'function_word_pct': 38}

    print("=== Normal scenario ===")
    combine_scores(keystroke_normal, mouse_normal, stylometry_normal)

    print("\n=== Drifted scenario ===")
    combine_scores(keystroke_drifted, mouse_drifted, stylometry_drifted)

    print("\n=== Borderline scenario ===")
    combine_scores(keystroke_borderline, mouse_borderline, stylometry_borderline)