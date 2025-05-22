# Refined Features for TEKS LMS

This document tracks all major features, their subcomponents, implementation progress, and the exact files/components involved for the TEKS LMS project. Each feature is broken down for clarity and project management, with actionable improvement notes. **No feature is marked as Done until explicitly set.**

---

## 1. User Roles & Permissions

- **Roles:** Student, Teacher, Admin

- **Subcomponents:**

  - Role-based navigation and dashboard ([frontend/src/app/page.tsx](../frontend/src/app/page.tsx), [frontend/src/app/components/NavBar.tsx](../frontend/src/app/components/NavBar.tsx))
  - Role-based page access (Add route guards/middleware in Next.js, e.g. `middleware.ts` or per-page logic)
  - Secure permissions enforcement (Backend: `backend/main.py`, Frontend: add checks to all page components)

- **Improvements:**
  - Refined role state management and ensured persistence via cookie in [frontend/src/app/page.tsx] (Complete)
  - Implemented Next.js middleware for route protection ([frontend/src/app/middleware.ts]) (Complete, improved type safety and role validation)
  - Modularized backend API using FastAPI routers ([backend/routers/assignments.py], [backend/routers/analytics.py], [backend/routers/users.py], [backend/routers/lessons.py], [backend/main.py]) (Complete)
  - Enforce permissions in backend API endpoints ([backend/main.py]) (Complete: see get_assignments, get_analytics)
  - Add tests for unauthorized access ([backend/test_permissions.py]) (Complete: see test_assignments_unauthorized, test_analytics_unauthorized)
  - Improved type safety for role state in middleware (Complete)

---

## 2. Student Experience

- **Dashboard:** ([frontend/src/app/components/dashboard/StudentDashboard.tsx](../frontend/src/app/components/dashboard/StudentDashboard.tsx))

  - Learning progress overview (Dynamic, fetches from backend /api/progress)
  - Helpful links to lessons (Static, planned: dynamic recommendations)
  - Assignments from teachers (Dynamic, fetches from backend)

- **Navigation:** lessons/, progress/, playground/, assignments/, chat/ ([frontend/src/app/lessons/page.tsx](../frontend/src/app/lessons/page.tsx), etc.)

- **Lessons:**

  - Guided Unity-based lessons ([frontend/public/unity/](../frontend/public/unity/), [frontend/src/app/lessons/page.tsx](../frontend/src/app/lessons/page.tsx))
  - AI-driven learning style adaptation (Backend: `backend/main.py`, AI agent in `backend/`, Frontend: add hooks/UI)

- **Playground:**

  - Interactive tools for practice ([frontend/src/app/playground/page.tsx](../frontend/src/app/playground/page.tsx))

- **Chat:**

  - Support agent with RAG context ([frontend/src/app/chat/page.tsx](../frontend/src/app/chat/page.tsx), Backend: `backend/ai_agent_notes.md`, `backend/main.py`)

- **Improvements:**
  - Integrate Unity WebGL player in lessons page (Planned)
  - Connect chat to backend support agent (Planned)
  - [x] Add progress tracking and feedback mechanisms (progress history bar chart, personalized feedback)
  - Ensure accessibility and responsive design (Planned)
  - [x] Student progress card now fetches from backend
  - [x] Assignments now fetched dynamically from backend
  - [x] Helpful links now fetched dynamically from backend recommendations endpoint

---

## 3. Teacher Experience

- **Dashboard:** ([frontend/src/app/components/dashboard/TeacherDashboard.tsx](../frontend/src/app/components/dashboard/TeacherDashboard.tsx))

  - Lesson builder UI
  - Student progress analytics
  - Assignment management

- **Lessons Page:** ([frontend/src/app/lessons/page.tsx](../frontend/src/app/lessons/page.tsx))

  - Interactive lesson plan builder
  - Assign lessons to students
  - Analyze learning gaps

- **Improvements:**
  - Build lesson builder UI (drag-and-drop, forms, templates)
  - Add analytics charts (use [frontend/public/unity/], or chart libs)
  - Enable real-time feedback on student progress
  - Streamline assignment creation and review

---

## 4. Admin Experience

- **Dashboard:** ([frontend/src/app/components/dashboard/AdminDashboard.tsx](../frontend/src/app/components/dashboard/AdminDashboard.tsx))

  - Redis-enabled analytics (Backend: `backend/main.py`, [infra/](../infra/))
  - User stats by type
  - Trends in learning types
  - Lesson popularity analytics
  - General website analytics

- **Improvements:**
  - Connect dashboard to backend analytics endpoints
  - Visualize data with charts (frontend)
  - Add filters and export options for analytics
  - Ensure data privacy and security compliance

---

## 5. Authentication & Security

- **OAuth2.0 system** (Backend: `backend/main.py`, Frontend: add login page/component)
- **Role-based access control**
- **Perfect security standards**

- **Improvements:**
  - Implement OAuth2.0 with secure token storage
  - Add login/logout UI ([frontend/src/app/](../frontend/src/app/))
  - Enforce HTTPS and secure cookies
  - Regularly audit dependencies and code for vulnerabilities

---

## 6. Backend & AI

- **FastAPI backend for all routes** (`backend/main.py`, `backend/requirements.txt`)
- **Python backend connected to Groq for AI** (`backend/main.py`, `backend/ai_agent_notes.md`)
- **AI-based learning type classification agent** (`backend/llm-agents/`, `backend/main.py`)
- **Support agent with RAG context** (`backend/ai_agent_notes.md`, `backend/main.py`)

- **Improvements:**
  - Define API endpoints for lessons, analytics, chat
  - Integrate Groq and RAG logic
  - Add automated tests for all endpoints
  - Document API with OpenAPI/Swagger

---

## 7. Content & Data

- **Database of TEKS standard content** (`backend/`, `infra/rds.tf`)
- **Database for user accounts** (`backend/`, `infra/rds.tf`)
- **Lesson generation from TEKS** (`backend/`, `frontend/src/app/lessons/page.tsx`)

- **Improvements:**
  - Seed TEKS data in DB
  - Build lesson generation API
  - Ensure data normalization and indexing for performance
  - Add migration scripts and backup strategies

---

## 8. Analytics

- **Redis-enabled analytics dashboard** (`backend/`, `infra/`, [frontend/src/app/components/dashboard/AdminDashboard.tsx](../frontend/src/app/components/dashboard/AdminDashboard.tsx))
- **Charts for user stats, learning types, lesson popularity** (Frontend: use chart library, e.g. Chart.js/Recharts)

- **Improvements:**
  - Connect frontend to analytics API
  - Add real-time charts
  - Implement role-based analytics views
  - Optimize Redis queries for performance

---

## 9. DevOps & Testing

- **CI/CD with GitHub Actions** (`.github/workflows/`, `nx.json`, `package.json`)
- **Nx monorepo integration** (`nx.json`, `package.json`, [frontend/](../frontend/), [backend/](../backend/))
- **End-to-end test suite** ([frontend-e2e/](../frontend-e2e/), Playwright)
- **Terraform AWS deployment** ([infra/](../infra/))

- **Improvements:**
  - Add more e2e tests (frontend-e2e/src/)
  - Complete Terraform scripts for AWS
  - Automate infrastructure provisioning and teardown
  - Monitor CI/CD pipeline health and test coverage

---

## 10. UI/UX

- **LeetCode-inspired design** ([frontend/src/app/](../frontend/src/app/), Tailwind CSS)
- **Responsive, modern UI** ([frontend/src/app/global.css](../frontend/src/app/global.css), Tailwind config)

- **Improvements:**
  - Refine dashboard layouts
  - Add more interactive/animated UI elements
  - Conduct user testing and gather feedback
  - Ensure accessibility (WCAG compliance)

---

## Backend/Frontend API Routing Standard

- **Backend API:**

  - All business logic, data access, and permissions enforcement must reside in modular FastAPI routers under `backend/routers/`.
  - Each router (e.g., `assignments.py`, `lessons.py`) exposes endpoints under a logical prefix (e.g., `/api/assignments`, `/api/lessons`).
  - The main FastAPI app (`backend/main.py`) mounts these routers with a `/api` prefix for all backend APIs.
  - The frontend (Next.js) fetches data from `/api/*` endpoints, which are reverse-proxied to the backend FastAPI server in production (or via a proxy in dev).
  - **Standard:** Never duplicate business logic in Next.js API routes. All critical data and permissions logic must be in FastAPI routers.
  - **Testing:** All backend endpoints must be covered by tests in `backend/test_permissions.py` or similar test files.

- **Frontend API:**

  - Next.js API routes (`frontend/src/app/api/*`) are reserved for frontend-only logic or edge functions (e.g., SSR helpers, auth callbacks) and should not duplicate backend business logic.
  - Use these only for logic that must run in the Next.js runtime (e.g., server actions, auth callbacks, or edge-specific code).
  - If a Next.js API route proxies to the backend, it must not contain business logic, only proxy logic.

- **Example:**

  - Frontend fetches assignments: `/api/assignments` (handled by FastAPI backend)
  - Frontend-only logic: `/api/hello` (handled by Next.js API route)
  - Frontend proxy logic: `/api/proxy/assignments` (Next.js API route proxies to backend, no business logic)

- **Action Items:**
  - Ensure all new backend endpoints are added as routers under `backend/routers/` and mounted in `backend/main.py` with `/api/` prefix.
  - Do not duplicate backend logic in Next.js API routes.
  - Document any exceptions in this file.
  - Add/maintain tests for all backend endpoints.

---

# Next Steps: Student Experience Improvements

## 2. Student Experience

- **Dashboard:** ([frontend/src/app/components/dashboard/StudentDashboard.tsx](../frontend/src/app/components/dashboard/StudentDashboard.tsx))

  - Learning progress overview (Dynamic, fetches from backend /api/progress)
  - Helpful links to lessons (Static, planned: dynamic recommendations)
  - Assignments from teachers (Dynamic, fetches from backend)

- **Navigation:** lessons/, progress/, playground/, assignments/, chat/ ([frontend/src/app/lessons/page.tsx](../frontend/src/app/lessons/page.tsx), etc.)

- **Lessons:**

  - Guided Unity-based lessons ([frontend/public/unity/](../frontend/public/unity/), [frontend/src/app/lessons/page.tsx](../frontend/src/app/lessons/page.tsx))
  - AI-driven learning style adaptation (Backend: `backend/main.py`, AI agent in `backend/`, Frontend: add hooks/UI)

- **Playground:**

  - Interactive tools for practice ([frontend/src/app/playground/page.tsx](../frontend/src/app/playground/page.tsx))

- **Chat:**

  - Support agent with RAG context ([frontend/src/app/chat/page.tsx](../frontend/src/app/chat/page.tsx), Backend: `backend/ai_agent_notes.md`, `backend/main.py`)

- **Improvements:**
  - Integrate Unity WebGL player in lessons page (Planned)
  - Connect chat to backend support agent (Planned)
  - [x] Add progress tracking and feedback mechanisms (progress history bar chart, personalized feedback)
  - Ensure accessibility and responsive design (Planned)
  - [x] Student progress card now fetches from backend
  - [x] Assignments now fetched dynamically from backend
  - [x] Helpful links now fetched dynamically from backend recommendations endpoint

---

# Implementation Progress

- [x] API routing standard documented and enforced
- [ ] Student Experience improvements (next up)

---

_This document will be updated as features are implemented or refined._
