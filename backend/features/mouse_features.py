import pandas as pd
import numpy as np


def extract_mouse_features(csv_path):
    df = pd.read_csv(csv_path)

    # Split click rows from movement rows (if the CSV has an event_type column)
    if 'event_type' in df.columns:
        clicks = df[df['event_type'] == 'click']
        move_df = df[df['event_type'] != 'click'].copy()
    else:
        clicks = df.iloc[0:0]
        move_df = df.copy()

    # Click features
    click_count = int(len(clicks))
    if click_count >= 2:
        avg_click_gap = float(clicks['timestamp'].diff().dropna().mean())
    else:
        avg_click_gap = 0.0

    # Not enough movement points
    if len(move_df) < 2:
        return {
            "avg_speed": 0.0,
            "click_count": click_count,
            "avg_click_gap": avg_click_gap,
            "path_straightness": 0.0,
        }

    # Consecutive point differences
    move_df["dx"] = move_df["x"] - move_df["x"].shift()
    move_df["dy"] = move_df["y"] - move_df["y"].shift()
    move_df["distance"] = np.sqrt(move_df["dx"] ** 2 + move_df["dy"] ** 2)
    move_df["dt"] = move_df["timestamp"] - move_df["timestamp"].shift()

    # Speed (ignore rows where dt is 0 to avoid divide-by-zero / infinity)
    valid = move_df["dt"] > 0
    speed = move_df.loc[valid, "distance"] / move_df.loc[valid, "dt"]
    avg_speed = float(speed.mean()) if len(speed) > 0 else 0.0

    # Path straightness
    start = move_df.iloc[0]
    end = move_df.iloc[-1]
    straight_distance = np.sqrt((end["x"] - start["x"]) ** 2 + (end["y"] - start["y"]) ** 2)
    total_distance = move_df["distance"].sum()
    path_straightness = float(straight_distance / total_distance) if total_distance > 0 else 0.0

    return {
        "avg_speed": avg_speed,
        "click_count": click_count,
        "avg_click_gap": avg_click_gap,
        "path_straightness": path_straightness,
    }