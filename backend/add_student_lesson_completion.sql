-- Add a table to log lesson completions for analytics and audit
CREATE TABLE IF NOT EXISTS student_lesson_completion (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    lesson_id INTEGER NOT NULL,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
