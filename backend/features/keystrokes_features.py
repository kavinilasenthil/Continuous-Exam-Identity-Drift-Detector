import pandas as pd

def extract_keystroke_features(csv_path):
    df = pd.read_csv(csv_path)

    avg_dwell_time = df['dwell_time'].mean()
    avg_flight_time = df['flight_time'].mean()

    total_keys = len(df)
    total_time_sec = (df['keydown_time'].max() - df['keydown_time'].min()) / 1000
    typing_speed = total_keys / total_time_sec

    return {
        'avg_dwell_time': avg_dwell_time,
        'avg_flight_time': avg_flight_time,
        'typing_speed': typing_speed
    }

if __name__ == '__main__':
    result = extract_keystroke_features('sample_keystrokes.csv')
    print(result)
