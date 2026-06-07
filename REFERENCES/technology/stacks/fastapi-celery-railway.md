# fastapi-celery-railway

Status: approved

Use this pattern for Python APIs, AI/data services, and background processing services on Railway.

## Core Stack

| Layer | Choice |
|-------|--------|
| API framework | FastAPI |
| Database | Postgres |
| ORM/migrations | SQLAlchemy + Alembic |
| Background jobs | Celery |
| Broker/cache | Redis |
| Deployment | Railway |
| Auth | authlib + python-jose when issuing app JWTs after OAuth |

## Use When

- The service does AI/data processing, transcription, extraction, ingestion, or scheduled work.
- Python libraries are central to the product.
- Background work should run outside request handlers.

## Consider Another Pattern When

- The project is primarily a web app. Use `nextjs-railway-docker`.
- The backend is a Node real-time service. Consider `express-node-railway` after review.
- The app is mobile only. Use `react-native-eas` for the app and this pattern only for its backend.

## Delivery Notes

- Document worker services separately from API services.
- Record Redis usage, retry behavior, and idempotency assumptions.
- Keep provider API keys in Railway variables or another approved secret store.
- Add health checks and logs before launch.
