# 🛠️ Sprint 1 (Setup Week)

Goal: Establish foundational infrastructure and development environments.

## Tasks:

✅ Initialize monorepo (package.json with workspaces)
✅ Scaffold frontend (React + Three.js base) and backend API (FastAPI)
✅ Set up CI/CD pipeline (GitHub Actions → AWS sandbox)
✅ Deploy hello-scene WebGL demo to staging via CDN (S3 + CloudFront)
✅ Provision initial LLM backend instance for testing (vLLM + dummy prompt)

## Deliverables:

✅ Working end-to-end skeleton: load WebGL scene from repo → CDN → browser
✅ Basic API endpoints for health checks and authentication
✅ LLM service with placeholder response generation
✅ Infrastructure as code (Terraform) for AWS resources

## Testing:

- Frontend: Verify WebGL scene loads correctly in browser
- Backend: Verify API endpoints return expected responses
- LLM Service: Verify placeholder responses are generated
- Infrastructure: Verify all resources are created and accessible

## Next Steps:

- Implement authentication with Google OAuth
- Create shared models and utilities
- Set up analytics pipeline with Redis/Kafka
- Implement content management system
<<<<<<< HEAD
- Begin building initial 3D assets
- NX setup for monorepo structure and workspaces
=======
>>>>>>> 816b753 (Initial Monorepo Scaffolding for EnableWeb)
