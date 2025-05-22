import React from 'react';

const NAV_LINKS = {
  Student: [
    { name: 'Lessons', href: '/lessons' },
    { name: 'Progress', href: '/progress' },
    { name: 'Playground', href: '/playground' },
    { name: 'Assignments', href: '/assignments' },
    { name: 'Chat', href: '/chat' },
  ],
  Teacher: [
    { name: 'Lessons', href: '/lessons' },
    { name: 'Progress', href: '/progress' },
    { name: 'Playground', href: '/playground' },
    { name: 'Assignments', href: '/assignments' },
    { name: 'Chat', href: '/chat' },
  ],
  Admin: [
    { name: 'Dashboard', href: '/' },
    { name: 'Analytics', href: '/analytics' },
    { name: 'Users', href: '/users' },
  ],
} as const;

type Role = keyof typeof NAV_LINKS;

export default function NavBar({
  role,
  setRole,
}: {
  role: Role;
  setRole: (r: Role) => void;
}) {
  return (
    <nav className="bg-white shadow sticky top-0 z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
        <div className="flex items-center gap-4">
          <span className="font-bold text-xl text-blue-600 tracking-tight">
            EnableWeb
          </span>
          <div className="hidden md:flex gap-2 ml-8">
            {NAV_LINKS[role].map((link) => (
              <a
                key={link.name}
                href={link.href}
                className="text-gray-700 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                {link.name}
              </a>
            ))}
          </div>
        </div>
        <div className="flex items-center gap-4">
          <select
            className="border rounded px-2 py-1 text-sm bg-gray-100"
            value={role}
            onChange={(e) => setRole(e.target.value as Role)}
            aria-label="Switch user role"
          >
            <option value="Student">Student</option>
            <option value="Teacher">Teacher</option>
            <option value="Admin">Admin</option>
          </select>
          <div className="w-8 h-8 rounded-full bg-blue-200 flex items-center justify-center font-bold text-blue-700">
            {role === 'Student' && 'S'}
            {role === 'Teacher' && 'T'}
            {role === 'Admin' && 'A'}
          </div>
        </div>
      </div>
    </nav>
  );
}
