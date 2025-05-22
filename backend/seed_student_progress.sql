-- SQL schema for student progress tracking

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

-- Seed data for demo student (student_id=1)
INSERT INTO student_progress (student_id, progress, message)
VALUES (1, 72, 'You\'re on track! Keep it up!')
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
