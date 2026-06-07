# nextjs-railway-docker

Status: default

Use this pattern for Xyric web apps, dashboards, portals, and internal tools that need a production web frontend with app-adjacent server logic.

## Core Stack

| Layer | Choice |
|-------|--------|
| Framework | Next.js 15/16 |
| Language | TypeScript |
| Database | Postgres |
| ORM/data access | Prisma by default; Drizzle or raw `pg.Pool` only when justified |
| Deployment | Railway |
| Packaging | Multi-stage Docker build |
| Auth | NextAuth v5 for new Next.js apps, or Google OAuth domain restriction for internal tools |

## Use When

- The product is a web app, admin dashboard, internal tool, or portal.
- The backend needs are app-adjacent and can live with the web service.
- Railway is an acceptable deployment target.

## Consider Another Pattern When

- The service is mostly Python, AI/data processing, transcription, or long-running background work. Use `fastapi-celery-railway`.
- The product is mobile-first. Use `react-native-eas`.
- The backend needs real-time Node services, heavy queues, or Socket.IO. Consider the candidate `express-node-railway` pattern after review.

## Common Variations

- Prisma 5 in existing projects.
- Prisma 7 adapter pattern in newer projects.
- Drizzle for dual SQLite/Postgres projects.
- Custom JWT/cookie auth for apps that do not fit NextAuth.

Record any variation in the project `tech-stack.md`.
