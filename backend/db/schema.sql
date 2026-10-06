CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('test_taker', 'test_maker'))
);

CREATE TABLE sessions (
    session_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE scores (
    score_id INTEGER PRIMARY KEY,
    session_id INTEGER NOT NULL,
    timestamp DATETIME NOT NULL,
    keystroke_score REAL,
    mouse_score REAL,
    stylometry_score REAL,
    fusion_score REAL,
    flagged INTEGER DEFAULT 0,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);