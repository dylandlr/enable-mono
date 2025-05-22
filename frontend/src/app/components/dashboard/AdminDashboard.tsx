import React from 'react';

export default function AdminDashboard() {
  return (
    <section>
      <h1 className="text-2xl font-bold mb-4">Admin Analytics Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="font-semibold mb-2">User Stats</h3>
          <div className="w-full h-20 bg-gray-100 rounded flex items-center justify-center text-gray-400">
            Redis Analytics
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="font-semibold mb-2">Learning Types Trends</h3>
          <div className="w-full h-20 bg-gray-100 rounded flex items-center justify-center text-gray-400">
            Trends Chart
          </div>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="font-semibold mb-2">Lesson Popularity</h3>
          <div className="w-full h-20 bg-gray-100 rounded flex items-center justify-center text-gray-400">
            Popularity Chart
          </div>
        </div>
      </div>
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="font-semibold mb-2">General Website Analytics</h3>
        <div className="w-full h-32 bg-gray-100 rounded flex items-center justify-center text-gray-400">
          Website Analytics
        </div>
      </div>
    </section>
  );
}
