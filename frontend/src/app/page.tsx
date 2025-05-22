'use client';

import React, { useState, useEffect } from 'react';
import NavBar from './components/NavBar';
import StudentDashboard from './components/dashboard/StudentDashboard';
import TeacherDashboard from './components/dashboard/TeacherDashboard';
import AdminDashboard from './components/dashboard/AdminDashboard';

export type Role = 'Student' | 'Teacher' | 'Admin';

export default function Index() {
  const [role, setRole] = useState<Role>('Student');

  // Persist role in cookie for middleware and reloads
  useEffect(() => {
    document.cookie = `role=${role}; path=/;`;
  }, [role]);

  return (
    <div className="min-h-screen bg-gray-50">
      <NavBar role={role} setRole={setRole} />
      <main className="max-w-7xl mx-auto py-8 px-4">
        {role === 'Student' && <StudentDashboard />}
        {role === 'Teacher' && <TeacherDashboard />}
        {role === 'Admin' && <AdminDashboard />}
      </main>
    </div>
  );
}
