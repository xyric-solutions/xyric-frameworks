# Stack Patterns

Stack patterns are reusable implementation recipes for Xyric software projects.

Use a pattern when it matches the project shape. If no pattern fits, record the reason in the project `tech-stack.md` and propose a new pattern only after the approach is likely to be reused.

## Patterns

| Pattern | Use it for |
|---------|------------|
| `nextjs-railway-docker.md` | Web apps, dashboards, portals, and internal tools on Railway. |
| `react-native-eas.md` | Expo React Native mobile apps built and shipped with EAS. |
| `fastapi-celery-railway.md` | Python APIs and AI/data services with async background work. |

## Pattern Quality Bar

Each pattern should state:

- when to use it
- when not to use it
- core technologies
- deployment target
- database/storage expectations
- auth expectations
- testing and observability expectations
- common variations
