#!/usr/bin/env python3
"""
Run this script to create the student_progress, student_progress_history, and student_lesson_completion tables and seed demo data in your Neon Postgres database using SQLAlchemy and your DATABASE_URL from .env.
"""
import os
import dotenv
from sqlalchemy import create_engine, text

dotenv.load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set. Please check your .env file.")
engine = create_engine(DATABASE_URL)

schema_sql = """
CREATE TABLE IF NOT EXISTS student_progress (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    progress INTEGER NOT NULL,
    message TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS student_progress_history (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    date DATE NOT NULL,
    progress INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS student_lesson_completion (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    lesson_id INTEGER NOT NULL,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

seed_sql = """
INSERT INTO student_progress (student_id, progress, message)
VALUES (1, 72, 'You''re on track! Keep it up!')
ON CONFLICT DO NOTHING;

INSERT INTO student_progress_history (student_id, date, progress) VALUES
(1, '2025-05-15', 60),
(1, '2025-05-16', 62),
(1, '2025-05-17', 65),
(1, '2025-05-18', 68),
(1, '2025-05-19', 70),
(1, '2025-05-20', 72),
(1, '2025-05-21', 72)
ON CONFLICT DO NOTHING;
"""

def main():
    with engine.begin() as conn:
        print("Creating tables...")
        conn.execute(text(schema_sql))
        print("Seeding demo data...")
        for stmt in seed_sql.strip().split(';'):
            if stmt.strip():
                conn.execute(text(stmt))
        print("Done.")

def test_db_connection():
    with engine.connect() as conn:
        print("Testing student_progress...")
        result = conn.execute(text("SELECT * FROM student_progress WHERE student_id=1"))
        for row in result.fetchall():
            print(dict(row._mapping))
        print("Testing student_progress_history...")
        result = conn.execute(text("SELECT * FROM student_progress_history WHERE student_id=1 ORDER BY date ASC"))
        for row in result.fetchall():
            print(dict(row._mapping))

if __name__ == "__main__":
    main()
    test_db_connection()
