import { NextRequest, NextResponse } from 'next/server';

// Example: Only allow access to certain routes for specific roles
// In a real app, you would check a session/cookie/JWT for the user's role

const protectedRoutes: Record<
  string,
  Array<'Student' | 'Teacher' | 'Admin'>
> = {
  '/assignments': ['Student', 'Teacher'],
  '/progress': ['Student', 'Teacher'],
  '/playground': ['Student', 'Teacher'],
  '/chat': ['Student', 'Teacher'],
  '/lessons': ['Student', 'Teacher', 'Teacher'],
  '/analytics': ['Admin'],
  '/users': ['Admin'],
  '/': ['Student', 'Teacher', 'Admin'],
};

function isValidRole(role: string): role is 'Student' | 'Teacher' | 'Admin' {
  return ['Student', 'Teacher', 'Admin'].includes(role);
}

export function middleware(request: NextRequest) {
  // Get role from cookie, fallback to 'Student' if invalid
  const cookieRole = request.cookies.get('role')?.value;
  const role = isValidRole(cookieRole || '') ? cookieRole : 'Student';
  const { pathname } = request.nextUrl;

  // Find the first matching protected route
  const matched = Object.keys(protectedRoutes).find((route) =>
    pathname.startsWith(route)
  );

  if (matched) {
    const allowedRoles = protectedRoutes[matched];
    if (!allowedRoles.includes(role as 'Student' | 'Teacher' | 'Admin')) {
      // Redirect to home or show unauthorized
      return NextResponse.redirect(new URL('/', request.url));
    }
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    '/assignments',
    '/progress',
    '/playground',
    '/chat',
    '/lessons',
    '/analytics',
    '/users',
    '/',
  ],
};
