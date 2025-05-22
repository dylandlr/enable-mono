import React, { useEffect, useState } from 'react';

interface Assignment {
  id: string;
  title: string;
  subject: string;
  due: string;
  status: 'due' | 'overdue' | 'completed';
}

export function useUpdateProgress() {
  return async (lessonId: number, increment = 1) => {
    const res = await fetch('/api/progress/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ lesson_id: lessonId, increment }),
    });
    return res.json();
  };
}

export default function StudentDashboard() {
  const [progress, setProgress] = useState<number | null>(null);
  const [progressMsg, setProgressMsg] = useState('');
  const [assignments, setAssignments] = useState<Assignment[]>([]);
  const [recommendations, setRecommendations] = useState<
    { label: string; href: string }[]
  >([]);
  const [progressHistory, setProgressHistory] = useState<
    { date: string; progress: number }[]
  >([]);
  const [feedback, setFeedback] = useState<string[]>([]);

  useEffect(() => {
    async function fetchProgress() {
      const res = await fetch('/api/progress');
      if (res.ok) {
        const data = await res.json();
        setProgress(data.progress);
        setProgressMsg(data.message);
      } else {
        setProgress(null);
        setProgressMsg('Unable to load progress.');
      }
    }
    async function fetchAssignments() {
      const res = await fetch('/api/assignments');
      if (res.ok) {
        const data = await res.json();
        setAssignments(data.assignments || []);
      } else {
        setAssignments([]);
      }
    }
    async function fetchRecommendations() {
      const res = await fetch('/api/progress/recommendations');
      if (res.ok) {
        const data = await res.json();
        setRecommendations(data.links || []);
      } else {
        setRecommendations([]);
      }
    }
    async function fetchProgressHistory() {
      const res = await fetch('/api/progress/history');
      if (res.ok) {
        const data = await res.json();
        setProgressHistory(data.history || []);
      } else {
        setProgressHistory([]);
      }
    }
    async function fetchFeedback() {
      const res = await fetch('/api/progress/feedback');
      if (res.ok) {
        const data = await res.json();
        setFeedback(data.feedback || []);
      } else {
        setFeedback([]);
      }
    }
    fetchProgress();
    fetchAssignments();
    fetchRecommendations();
    fetchProgressHistory();
    fetchFeedback();
  }, []);

  return (
    <section>
      <h1 className="text-2xl font-bold mb-4">Welcome back, Student!</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {/* Progress Card */}
        <div
          className="bg-white rounded-lg shadow p-6 flex flex-col items-center"
          aria-label="Learning Progress"
          tabIndex={0}
        >
          <span className="text-lg font-semibold mb-2">Learning Progress</span>
          <div className="w-24 h-24 rounded-full bg-blue-100 flex items-center justify-center mb-2">
            <span className="text-3xl font-bold text-blue-600">
              {progress !== null ? `${progress}%` : '--'}
            </span>
          </div>
          <span className="text-gray-500 text-sm">
            {progressMsg || 'Loading...'}
          </span>
          {progressHistory.length > 0 && (
            <div
              className="mt-4 w-full"
              aria-label="Progress History Bar Chart"
            >
              <span className="block text-xs text-gray-400 mb-1">
                Last 7 days:
              </span>
              <div className="flex gap-1 items-end h-12">
                {progressHistory.map((h) => (
                  <div
                    key={h.date}
                    className="flex-1 flex flex-col items-center"
                  >
                    <div
                      className="w-2 rounded bg-blue-400"
                      style={{ height: `${h.progress / 2}%`, minHeight: 4 }}
                      title={`${h.progress}% on ${h.date}`}
                      aria-label={`Progress ${h.progress}% on ${h.date}`}
                    ></div>
                    <span className="text-[10px] text-gray-400 mt-1">
                      {h.date.slice(5)}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          )}
          {feedback.length > 0 && (
            <ul
              className="mt-2 w-full text-xs text-blue-700 bg-blue-50 rounded p-2"
              aria-label="Personalized Feedback"
            >
              {feedback.map((msg, i) => (
                <li key={i} className="mb-1">
                  {msg}
                </li>
              ))}
            </ul>
          )}
        </div>
        {/* Assignments Card */}
        <div
          className="bg-white rounded-lg shadow p-6 flex flex-col items-center"
          aria-label="Assignments"
          tabIndex={0}
        >
          <span className="text-lg font-semibold mb-2">Assignments</span>
          <ul className="w-full text-left text-sm">
            {assignments.length === 0 && <li>No assignments found.</li>}
            {assignments.map((a) => (
              <li key={a.id} className="mb-1 flex justify-between">
                <span>
                  {a.subject}: {a.title}
                </span>
                <span
                  className={
                    a.status === 'overdue'
                      ? 'text-red-600'
                      : a.status === 'due'
                      ? 'text-yellow-600'
                      : 'text-green-600'
                  }
                >
                  {a.status === 'overdue' ? 'Overdue' : `Due: ${a.due}`}
                </span>
              </li>
            ))}
          </ul>
          <a
            href="/assignments"
            className="mt-3 text-blue-600 hover:underline text-sm"
          >
            View all assignments
          </a>
        </div>
        {/* Helpful Links Card */}
        <div
          className="bg-white rounded-lg shadow p-6 flex flex-col items-center"
          aria-label="Helpful Links"
          tabIndex={0}
        >
          <span className="text-lg font-semibold mb-2">Helpful Links</span>
          <ul className="w-full text-left text-sm">
            {recommendations.length === 0 && <li>Loading...</li>}
            {recommendations.map((link) => (
              <li key={link.href}>
                <a href={link.href} className="text-blue-600 hover:underline">
                  {link.label}
                </a>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
