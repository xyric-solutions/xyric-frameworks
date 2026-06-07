---
name: SPEC-DATA
parent: EXPERT-14
description: Generate data model specifications from user stories — entities, schema, migrations, validation.
version: "1.0"
domain: Data layer design and entity relationships
---

# Data Model Specs (SPEC-DATA)

> Sub-skill of [Story Spec Generator (EXPERT-14)](../SKILL.md)

## Focus Area

Transforms user story requirements into complete data model specifications. Covers entity definitions, database schema (SQL), relationships, migration plans, data validation rules, and indexing strategies. Does NOT cover API endpoint design or UI component structure — defer those to SPEC-API and SPEC-UI respectively.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Entity Design | TypeScript interfaces, field definitions, enums, constraints |
| Schema Design | SQL DDL, column types, defaults, foreign keys, unique constraints |
| Relationships | 1:1, 1:N, N:M mappings, junction tables, cascading rules |
| Migration Planning | Step-by-step migration with rollback strategy, data seeding |
| Indexing & Performance | Index selection, query pattern analysis, denormalization decisions |

## Methodology

### Priority Order
1. Identify all entities and their fields from acceptance criteria
2. Define relationships before field details — structure shapes constraints
3. Plan migrations with rollback — every schema change must be reversible
4. Validate against the existing data model recorded in the planning/status file and prior specs

### Workflow
1. Extract entities implied by the story (nouns = entities, verbs = relationships)
2. Define TypeScript interfaces with field types, descriptions, and constraints
3. Write SQL DDL with proper types, defaults, foreign keys, and indexes
4. Map entity relationships with cardinality notation
5. Create migration plan with ordered steps and rollback procedures

## Key Patterns

**Entity-First Thinking**: Start with the domain model. Entities come from the story's nouns. Fields come from acceptance criteria. Relationships come from how entities interact.

**Explicit Field Constraints**: Every field declares type, nullability, defaults, max length, and validation rules. No implicit assumptions — the schema IS the documentation.

**Migration Safety**: Every migration step has a rollback. Additive changes are safe; destructive changes (drop column, change type) require data migration scripts.

**Indexing by Access Pattern**: Create indexes based on query access patterns — every WHERE, JOIN, and ORDER BY should have supporting indexes.

**Audit Trail Awareness**: Sensitive entities include `created_at`, `updated_at`, `created_by`. Use soft deletes (`deleted_at`) when data retention matters.

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Entities without field definitions | Every entity has complete TypeScript interface + SQL DDL |
| Missing migration rollback | Every migration step has explicit rollback procedure |
| Indexes on every column | Index only columns used in queries (WHERE, JOIN, ORDER BY) |
| Ignoring existing schema | Check the planning/status file and prior specs for existing entities first |

## Quality Gates

| Gate | Target |
|------|--------|
| Entity completeness | All story nouns mapped to entities with full field definitions |
| Relationship clarity | All relationships documented with cardinality |
| Migration reversibility | Every step has a rollback action |
| Data validation | All user-input fields have validation rules defined |

## Deep Reference

For detailed patterns and code examples in this domain:
- Parent skill: `../SKILL.md` (full tech-spec philosophy, cross-skill integration)
- Reference sections: `../reference.md` → Q2: Data Model questions, Phase 2 generation
- Checklists: `../forms.md` → Section 4: Data Models, Migration Plan

## Team Integration

This sub-skill is designed for use in:
- **Product Development Team** — as the data architecture specialist
- Pairs well with: SPEC-API (entity shapes drive response schemas), SPEC-UI (data validation rules inform form validation)
