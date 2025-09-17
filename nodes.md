What I’ll Learn from Mini Workflow Runner

FastAPI
• Creating and organizing a FastAPI app.
• Defining routes with path and query parameters.
• Request/response validation with Pydantic.
• Middleware (CORS, logging).
• Background tasks and startup events.

Pydantic
• Building request/response models with validation rules.
• Schema nesting (workflow → nodes → configs).
• Serialization to JSON for API responses.
• Input validation errors and how FastAPI handles them.

SQLAlchemy
• Setting up engine, session, and declarative Base.
• Defining models with different column types (UUID, JSON, timestamps).
• Relationships (Workflow → Execution → Steps).
• Writing CRUD functions with sessions.
• Querying with filters and joins.

Alembic
• Initializing migrations in a project.
• Generating and applying schema migrations.
• Keeping DB schema in sync with models.

Database design
• Designing tables for workflows, executions, and steps.
• Storing structured JSON vs normalized tables.
• Using timestamps and status fields to track process state.
• Idempotency keys for safe retries.

Worker logic
• Looping over workflow definition and executing step by step.
• Handling success/failure states and logging outputs.
• Implementing per-step timeouts.
• Using async vs sync execution.
• Building small, pluggable “node handlers.”

HTTP & external calls
• Using httpx for async HTTP requests.
• Safe request/response handling and error catching.
• Understanding retries and timeouts.

Templates & transforms
• Using Jinja2 for safe data transforms.
• Passing context data between steps.

Logging & monitoring
• Structured logging for backend services.
• Recording detailed step-level execution logs.

Testing
• Unit testing Pydantic models.
• Integration testing FastAPI endpoints.
• Mocking HTTP requests.
• Verifying database state after workflow runs.

Frontend (React + Vite)
• Bootstrapping a Vite + React app.
• Setting up React Router for multiple pages.
• Building forms and controlled components.
• Calling backend APIs and handling JSON responses.
• Polling APIs for long-running processes (execution status).
• Displaying dynamic lists of workflow steps.

Full-stack integration
• Handling CORS between frontend and backend.
• Running both dev servers together (backend on 8000, frontend on 3000).
• Testing end-to-end flows manually.

Dev workflow & ops
• Writing clear README and docs for a project.
• Using environment variables for DB and secrets.
• Dockerizing backend + Postgres for consistent dev setup.
• CI basics (GitHub Actions for running tests).
