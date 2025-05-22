import React from 'react';

export default function TeacherDashboard() {
  return (
    <section>
      <h1 className="text-2xl font-bold mb-4">Teacher Dashboard</h1>
      <div className="bg-white rounded-lg shadow p-6 mb-8">
        <h2 className="text-xl font-semibold mb-2">Lesson Builder</h2>
        <p className="mb-2">
          Create and assign interactive lessons. Analyze student progress and
          learning gaps below.
        </p>
        {/* Placeholder for interactive lesson builder UI */}
        <div className="w-full h-32 bg-gray-100 rounded flex items-center justify-center text-gray-400">
          Lesson Builder UI
        </div>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="font-semibold mb-2">Student Progress Overview</h3>
          <div className="w-full h-24 bg-gray-100 rounded flex items-center justify-center text-gray-400">
            Progress Chart
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="font-semibold mb-2">Assignments</h3>
          <div className="w-full h-24 bg-gray-100 rounded flex items-center justify-center text-gray-400">
            Assignment List
          </div>
        </div>
      </div>
    </section>
  );
}
