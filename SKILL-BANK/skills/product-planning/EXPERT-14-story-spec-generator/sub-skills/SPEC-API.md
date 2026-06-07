---
name: SPEC-API
parent: EXPERT-14
description: Generate API contract specifications from user stories — endpoints, schemas, auth, errors.
version: "1.0"
domain: API contracts and endpoint design
---

# API Contract Specs (SPEC-API)

> Sub-skill of [Story Spec Generator (EXPERT-14)](../SKILL.md)

## Focus Area

Transforms user story acceptance criteria into complete API contract definitions. Covers endpoint design, request/response schemas, authentication requirements, rate limits, and error codes. Does NOT cover database schema, UI components, or state management — defer those to SPEC-DATA and SPEC-UI respectively.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Endpoint Design | RESTful resource naming, HTTP methods, URL structure, versioning |
| Schema Definition | TypeScript interfaces for request/response, field types, optionality |
| Error Contracts | HTTP status codes, error code taxonomy, user-facing messages |
| Security Contracts | Auth method selection, authorization rules, rate limiting policies |

## Methodology

### Priority Order
1. Map every acceptance criterion to at least one endpoint
2. Define auth/authz before writing schemas — security shapes the contract
3. Error paths before happy paths — robust APIs handle failure first
4. Consistency with existing API conventions in the product

### Workflow
1. Extract operations implied by the story (CRUD, search, actions)
2. Design endpoint structure following product API style (REST/GraphQL/tRPC)
3. Define request schemas with validation constraints
4. Define success and error response schemas
5. Document error codes, rate limits, and auth requirements

## Key Patterns

**API-First Design**: Define the contract before any implementation. The API contract is the agreement between frontend and backend teams — it must be unambiguous.

**Consistent Error Taxonomy**: Use a product-wide error code format (`DOMAIN_ACTION_ERROR`) with human-readable messages. Every endpoint documents its specific error cases.

**Schema Completeness**: Every field has a type, description, and constraints. Optional fields are explicitly marked. No `any` types allowed.

**Auth-Aware Design**: Each endpoint declares its auth requirement (public, authenticated, role-specific). Authorization rules are per-action, not per-endpoint. Use `/api/v1/` prefix; breaking changes require version bump.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Endpoints with no error documentation | Document all 4xx/5xx responses per endpoint |
| Vague field types (`data: object`) | Use explicit TypeScript interfaces with named fields |
| Missing rate limit consideration | Declare rate limiting tier for every write endpoint |
| Designing endpoints around UI views | Design around resources and operations |

## Quality Gates

| Gate | Target |
|------|--------|
| Acceptance criteria coverage | 100% of AC mapped to endpoints |
| Schema completeness | All fields typed, described, constrained |
| Error code specificity | No generic 500-only error handling |
| Auth documentation | Every endpoint declares auth requirement |

## Deep Reference

For detailed patterns and code examples in this domain:
- Parent skill: `../SKILL.md` (full tech-spec philosophy, cross-skill integration)
- Reference sections: `../reference.md` → Phase 2: Tech Spec Generation
- Checklists: `../forms.md` → Section 3: API Contracts, Error Codes table

## Team Integration

This sub-skill is designed for use in:
- **Product Development Team** — as the API design specialist
- Pairs well with: SPEC-DATA (entity definitions inform response shapes), SPEC-UI (component data needs drive endpoint design)
