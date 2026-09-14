import pandas as pd
import numpy as np

def extract_mouse_features(csv_path):
    # CSV read karo
    df = pd.read_csv(csv_path)

    # Movement dataframe
    move_df = df.copy()

    # Consecutive point differences
    move_df["dx"] = move_df["x"] - move_df["x"].shift()
    move_df["dy"] = move_df["y"] - move_df["y"].shift()

    # Distance
    move_df["distance"] = np.sqrt(
        move_df["dx"]**2 +
        move_df["dy"]**2
    )

    # Time difference
    move_df["dt"] = (
        move_df["timestamp"] -
        move_df["timestamp"].shift()
    )

    # Speed
    move_df["speed"] = (
        move_df["distance"] /
        move_df["dt"]
    )

    # Feature 1
    avg_speed = move_df["speed"].mean()

    # Feature 2 (Current CSV has no click events)
    click_count = 0

    # Feature 3
    avg_click_gap = 0

    # Feature 4
    start = move_df.iloc[0]
    end = move_df.iloc[-1]

    straight_distance = np.sqrt(
        (end["x"] - start["x"])**2 +
        (end["y"] - start["y"])**2
    )

    total_distance = move_df["distance"].sum()

    path_straightness = (
        straight_distance / total_distance
        if total_distance > 0 else 0
    )

    return {
        "avg_speed": avg_speed,
        "click_count": click_count,
        "avg_click_gap": avg_click_gap,
        "path_straightness": path_straightness
    }