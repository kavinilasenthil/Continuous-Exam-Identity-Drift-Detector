import pytest
from fusion_engine import combine_scores


def test_normal_case():
    keystroke = {'typing_speed': 4.4}
    mouse = {'avg_speed': 245}
    stylometry = {'Flesch Reading Ease': 53}

    score = combine_scores(keystroke, mouse, stylometry)
    assert 0.8 <= score <= 1.2


def test_drifted_case():
    keystroke = {'typing_speed': 1.0}
    mouse = {'avg_speed': 50}
    stylometry = {'Flesch Reading Ease': 15}

    score = combine_scores(keystroke, mouse, stylometry)
    assert score < 0.8


def test_missing_key():
    keystroke = {}
    mouse = {'avg_speed': 200}
    stylometry = {'Flesch Reading Ease': 50}

    with pytest.raises(KeyError):
        combine_scores(keystroke, mouse, stylometry)