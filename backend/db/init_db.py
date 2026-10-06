import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'exam_drift.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

# Remove old DB if it exists, so re-running this script starts fresh
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Load and run schema.sql to create the tables
with open(SCHEMA_PATH, 'r') as f:
    schema_sql = f.read()
cursor.executescript(schema_sql)

# Insert one dummy user
cursor.execute(
    "INSERT INTO users (user_id, name, role) VALUES (?, ?, ?)",
    (1, "Jane Doe", "test_taker")
)

# Insert one dummy session linked to that user
cursor.execute(
    "INSERT INTO sessions (session_id, user_id, start_time, end_time) VALUES (?, ?, ?, ?)",
    (1, 1, "2026-10-06 10:00:00", "2026-10-06 11:00:00")
)

# Insert one dummy score linked to that session
cursor.execute(
    """INSERT INTO scores
       (score_id, session_id, timestamp, keystroke_score, mouse_score, stylometry_score, fusion_score, flagged)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
    (1, 1, "2026-10-06 10:30:00", 0.92, 0.88, 0.95, 0.91, 0)
)

conn.commit()

# Query and print all rows from all three tables to confirm links work
print("=== USERS ===")
for row in cursor.execute("SELECT * FROM users"):
    print(row)

print("\n=== SESSIONS ===")
for row in cursor.execute("SELECT * FROM sessions"):
    print(row)

print("\n=== SCORES ===")
for row in cursor.execute("SELECT * FROM scores"):
    print(row)

conn.close()