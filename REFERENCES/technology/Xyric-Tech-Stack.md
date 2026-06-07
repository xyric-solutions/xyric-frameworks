---
type: technology-reference
title: Xyric Tech Stack Guide
status: Active
owner: CTO
last_updated: 2026-06-07
source_migrated_from: Xyric-Tech-Stack.md
source_last_updated: 2026-04-20
audience: Xyric employees, contractors, and AI agents working on Xyric software projects.
---

# Xyric Tech Stack Guide

This is the reusable Xyric technology reference for new and existing software projects.

Use it to answer:

- What should we use by default?
- What alternatives are already approved?
- When is a different tool acceptable?
- What needs project-owner review before use?

This guide is intentionally not a live product inventory. Keep per-project diagrams, repository paths, deployment service names, and provider env var catalogs in the relevant project docs or internal wiki.

## Agent Contract

When building, planning, reviewing, or refactoring Xyric software:

1. Read this document before recommending a stack.
2. Use the `Default` choice unless the project context clearly fits an approved alternative.
3. If a row says `Decision needed`, ask the project owner or record the missing decision.
4. Do not introduce new frameworks, databases, vendors, hosting platforms, auth providers, or AI providers without explaining why the default does not fit.
5. If the target project already has a stack, preserve it unless the task is explicitly about migration or replacement.
6. If you add or change a provider, dependency, database, queue, deployment target, or auth mechanism, update the project's own `tech-stack.md` in the same work.

## Decision Labels

| Label | Meaning |
|-------|---------|
| `Default` | Use this for new projects unless there is a strong reason not to. |
| `Approved alternative` | Allowed when the stated condition applies. |
| `Evaluate first` | Can be considered, but requires project-owner review. |
| `Avoid` | Do not use for new work unless explicitly approved. |
| `Decision needed` | The previous source did not define a reusable default. |

## Canonical Stack

| Area | Default | Approved alternatives | Use when | Avoid / needs review | Notes |
|------|---------|-----------------------|----------|----------------------|-------|
| Web frontend | Next.js 15/16 with TypeScript, Dockerized for Railway | Existing project stack; client-mandated frontend after review | Web apps, dashboards, portals, internal tools, product frontends | New web framework without review | Common pattern: `nextjs-railway-docker`. |
| Mobile app | Expo SDK 54 with React Native, EAS Build, and OTA updates | Native iOS/Android only after review | iOS/Android apps and mobile-first products | Unmanaged native split unless the project needs it | Common pattern: `react-native-eas`. |
| Backend/API | Match workload: Next.js app APIs for web-adjacent logic; FastAPI for Python/AI/data services | Express/Node 20 for real-time JS services; existing project stack | APIs, business logic, integrations, AI processing, background jobs | New backend framework without review | Common backend patterns: `fastapi-celery-railway`, candidate `express-node-railway`. |
| Hosting/deployment | Railway with Dockerized services | Expo EAS for mobile builds and updates | Web apps, APIs, workers, dashboards, backend services | Vercel/Fly/AWS/GCP/Azure without review | Railway auto-deploy from `main` is the default pattern for Railway projects. |
| Database | Postgres for production, preferably Railway-managed for Railway projects | SQLite only for local/dev or deliberate dual-dialect apps; NoSQL only for an explicitly approved NoSQL-specific use case | Primary application data | NoSQL as the primary production database without review | Previous portfolio standard: Postgres everywhere; NoSQL is not a production default. |
| ORM/data access | Choose by stack: Prisma for Next.js, SQLAlchemy + Alembic for FastAPI | Drizzle for dual SQLite/Postgres needs; raw `pg.Pool` for focused Node services | Schema-managed app data | Mixing ORMs in one service without review | Existing variations include Prisma 5, Prisma 7 adapter, Drizzle, raw `pg.Pool`, and SQLAlchemy. |
| Vector search | Postgres with `pgvector` where vector search is needed | Float-array fallback when `pgvector` is unavailable | Embeddings, semantic search, retrieval, AI memory | Separate vector DB without review | Use graceful fallback when deployment support is uncertain. |
| Auth | Google OAuth with `@xyric.ai` domain restriction for internal tools; NextAuth v5 for Next.js apps | Custom JWT + bcrypt + httpOnly cookies; expo-auth-session; authlib + python-jose | Internal tools, web login, mobile login, API-issued app JWTs | New auth provider without review | NextAuth v4 is existing-project only unless there is a migration reason. |
| Authorization model | Decision needed per project | RBAC, custom roles, admin-only gates | Roles, permissions, admin access, policy checks | Shipping without documented authorization rules | Record roles and permission boundaries in project docs. |
| Background jobs/queues | Redis-backed queues when async work is needed | Celery/Redis for Python; BullMQ/ioredis for Node; Upstash Redis for rate limiting | Transcription, ingestion, scheduled jobs, notifications, long tasks | Long-running work inside request handlers | Keep broker, retry, and idempotency behavior in project docs. |
| File/object storage | Cloudflare R2 for app uploads and S3-compatible storage | AWS S3 for audio/transcript storage or existing services | Images, documents, certificates, audio, transcripts, generated files | Local filesystem storage in production | Never commit storage credentials. |
| CI/CD | Railway auto-deploys from `main`; GitHub Actions for PR lint/test where configured | EAS Build manually or through CI for mobile | Builds, tests, deployments, previews | Production deploy path without checks | New projects should define required PR checks before launch. |
| Testing | Decision needed per project | Unit, integration, API, browser, mobile, and end-to-end tests as appropriate | Quality gates and regression protection | No test plan for launch-stage products | Minimum coverage depends on product risk and lifecycle stage. |
| Observability | Railway service logs | Sentry/error tracking and APM after review | Logs, errors, uptime, traces, metrics, alerts | Silent production failures | Centralized logging, Sentry, and APM are not standardized yet. |
| Email/messaging | Decision needed per project | Resend for transactional email; SMTP via nodemailer or fastapi-mail; Twilio for WhatsApp/voice | Transactional email, notifications, OTP/magic-link delivery, voice | Stubbed delivery in production | Choose delivery provider before user-facing rollout. |
| Payments/billing | Stripe for subscription billing | PayPal as alternative payment method | Checkout, subscriptions, invoices, webhooks | New payment processor without review | Payment work needs webhook and compliance review. |
| AI/LLM providers | Approved providers by task: Anthropic, OpenAI, Google Gemini | DeepSeek as fallback where already integrated | Reasoning, extraction, summaries, chat, embeddings, classification, video analysis | New model/provider without review | See AI provider guidance below. |
| Speech/voice | Deepgram for real-time speech-to-text | OpenAI Whisper fallback; AssemblyAI, ElevenLabs, Twilio for voice workflows | Transcription, voice calls, coaching, text-to-speech | New speech provider without review | Choose by latency, language support, cost, and privacy needs. |
| Analytics | Decision needed | Project-specific product analytics after review | Funnels, event tracking, reporting | Adding trackers without privacy review | The source doc did not define a standard analytics stack. |
| Documentation | Each product or app should maintain its own `tech-stack.md` | Architecture diagrams and provider tables in project docs | Onboarding, handoff, audits, AI orientation | Stack changes without doc updates | Framework docs define defaults; project docs define reality. |
| Design/UI system | Decision needed | Project or client design system | Components, tokens, layouts, icons, brand fit | New component library without review | The source doc did not define a reusable UI standard. |
| Package/runtime management | Use the runtime required by the chosen pattern | Node 20 for Express/Node services; Expo SDK 54 for mobile; Python for FastAPI services | Versioning, lockfiles, runtime setup | Unpinned major upgrades without review | Record exact versions in each project. |

## Stack Patterns

Reusable stack patterns should live under `REFERENCES/technology/stacks/`.

| Pattern | Status | Summary |
|---------|--------|---------|
| [`nextjs-railway-docker`](stacks/nextjs-railway-docker.md) | Default | Next.js 15/16 + ORM + Postgres + multi-stage Docker on Railway. |
| [`react-native-eas`](stacks/react-native-eas.md) | Default for mobile | Expo SDK 54 + EAS Build + OTA updates. |
| [`fastapi-celery-railway`](stacks/fastapi-celery-railway.md) | Approved | FastAPI + SQLAlchemy + Celery/Redis + Postgres on Railway. |
| `express-node-railway` | Candidate | Express 5 + Node 20 + Socket.IO/BullMQ + Postgres. Promote when reused by a second project. |

## AI Provider Guidance

| Capability | Preferred provider(s) | Notes |
|------------|-----------------------|-------|
| Reasoning, extraction, summaries | Anthropic Claude, OpenAI | Use based on quality, latency, price, and existing project integration. |
| Chat and general app AI | OpenAI, Anthropic Claude, Google Gemini | Keep model names configurable through env vars. |
| Embeddings | OpenAI `text-embedding-3-large` or project-approved equivalent | Store embeddings in Postgres/pgvector unless a separate vector DB is approved. |
| Classification and flow reasoning | Google Gemini, OpenAI, Anthropic Claude | Pick by evaluation results, not provider preference alone. |
| Video analysis | Google Gemini | Existing source identified Gemini for video-oriented analysis. |
| Speech-to-text | Deepgram for real-time, OpenAI Whisper fallback, AssemblyAI where already integrated | Use real-time providers for live transcription. |
| Text-to-speech / voice | ElevenLabs, Twilio | Document cost, voice, consent, and region constraints. |

Never commit API keys or secret values. Store values in Railway service variables, EAS secrets, GitHub Actions secrets, or local `.env` files that are ignored by git. It is acceptable to document env var names in project docs when that helps onboarding.

## External Provider Rule

If a project adds a new external provider:

1. Add it to the project's `tech-stack.md`.
2. Record the purpose, owner, data sent, environments used, and secret storage location.
3. Add required env var names, but never values.
4. Note any privacy, compliance, cost, or rate-limit concerns.
5. Update this guide only if the provider becomes a reusable Xyric default or approved alternative.

## Minimum New Project Record

Every new software project should document these before implementation starts:

| Decision | Required output |
|----------|-----------------|
| App type | Web app, mobile app, backend service, automation, data workflow, or mixed. |
| Stack pattern | One of the approved patterns, or a written reason for a new pattern. |
| Frontend | Framework, routing, styling/UI system, rendering approach, and deployment target. |
| Backend | Runtime, API framework, background jobs, queue/broker, and integration pattern. |
| Data | Primary database, ORM/data access, migrations, backups, vector needs, and file storage. |
| Auth | Identity provider, session/JWT model, authorization pattern, and admin access. |
| Delivery | Hosting, environments, CI/CD, preview flow, and required release checks. |
| Quality | Test types, browser/device coverage, monitoring, logging, and error handling. |
| Providers | AI, email, payment, storage, analytics, speech, and data APIs with env var names only. |
| AI/data handling | Model/provider, data retention, eval plan, human review points, and privacy constraints. |

## Project `tech-stack.md` Expectations

Project-level stack docs should include:

- YAML frontmatter with `title`, `status`, `owner`, and `last_updated`.
- Architecture and deployment diagrams when useful.
- Stack pattern used, including intentional deviations.
- Frameworks, runtimes, database, auth, storage, queues, and deployment targets.
- External integrations and API providers with env var names only.
- Known gaps and decisions needed before launch.

## What Was Not Migrated From The Old Wiki Page

The previous document also contained a portfolio diagram, project matrix, repository paths, deployment service inventory, and a large per-project API/provider catalog. Those are useful operational records, but they do not belong in this public reusable framework repo.

Keep that material in internal product docs or a private wiki. This reference keeps only reusable decisions, approved patterns, and rules that should travel across projects.

## Review Cadence

Review this reference:

- Quarterly.
- Whenever a default technology changes.
- Whenever a tool becomes unsupported, too expensive, or risky.
- When a new framework, database, hosting platform, AI provider, auth provider, or payment provider becomes reusable across projects.
- Before starting a major new product or migration.
