---
name: STORY-VALIDATE
parent: EXPERT-13
description: Validate story coverage, dependency integrity, persona mapping, and gap analysis against the Epic PRD
version: "1.0"
domain: Story coverage validation and gap analysis
---

# Story Coverage Validation (STORY-VALIDATE)

> Sub-skill of [Story Generator (EXPERT-13)](../SKILL.md)

## Focus Area

Specializes in verifying that a set of stories achieves 100% Epic feature coverage, that
dependencies form a valid DAG, that all personas are served, and that no gaps or duplicates
exist. Produces coverage matrices and gap reports. Does NOT create or split stories (use
STORY-DECOMPOSE) or write story content.

The story-linking field used to confirm task-to-story traceability is decided per
organization (see the parent's [`ADAPT.md`](../ADAPT.md)); ask via the parent's Workspace &
Conventions Intake if not yet decided.

## Core Competencies

| Skill Area | Focus |
|------------|-------|
| Coverage Matrix | Feature-to-story mapping with completeness percentage |
| Dependency Verification | DAG validation, circular-dependency detection, sequencing checks |
| Persona Mapping | Every persona served by the Epic has stories addressing their needs |
| Gap Analysis | Identify uncovered features, missing error scenarios, cross-cutting gaps |
| Duplicate Detection | Find overlapping story scopes that should be merged or differentiated |

## Methodology

### Priority Order
1. Coverage first — every Epic feature must map to at least one story
2. No orphans — every story must trace back to a feature
3. Personas must be served — each persona in the Epic has relevant stories
4. Dependencies must be acyclic — a single circular dependency blocks validation

### Workflow
1. **Map** — build the Feature → Story matrix from Epic PRD features and existing stories
2. **Check Coverage** — verify every feature (F[X.Y]) has >=1 story; flag gaps
3. **Check Duplicates** — compare story scopes pairwise; flag overlaps >30% similarity
4. **Verify Dependencies** — walk the dependency graph; confirm DAG (no cycles)
5. **Verify Personas** — cross-reference Epic personas with story user-story statements
6. **Report** — generate a validation report with pass/fail per check, a gap list, and
   recommendations

## Key Patterns

- **100% Coverage Rule** — all stories combined must implement the complete Epic. A single
  uncovered feature blocks validation.
- **Bidirectional Tracing** — check both directions: features without stories (gaps) AND
  stories without features (orphans)
- **Cross-Cutting Concerns** — security, accessibility, and performance requirements must
  appear in relevant stories, not be assumed
- **Persona Coverage Matrix** — build a secondary matrix (Persona × Feature) showing which
  stories serve which persona for which feature
- **Template Compliance** — verify all required template sections are present in each story
  file (YAML frontmatter, User Story, Scope, Acceptance Criteria, etc., per the configured
  template)

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|--------------|-----------------|
| Assuming coverage from story titles alone | Read story scope descriptions to verify actual coverage |
| Skipping the duplicate check for small Epics | Even 3-story Epics can have scope overlaps |
| Treating validation as optional | Validation is a blocking gate — no output without passing |
| Fixing gaps by expanding existing stories | Report gaps for STORY-DECOMPOSE to create new stories |

## Quality Gates

| Gate | Target |
|------|--------|
| Feature coverage | 100% of Epic features mapped to stories |
| Duplicate score | 0 overlapping story scopes |
| DAG validity | Zero circular dependencies |
| Persona coverage | Every Epic persona appears in >=1 story |
| Template compliance | All stories have the required template sections |

## Deep Reference

- Parent skill: `../SKILL.md` (full philosophy and validation gate)
- Reference: `../reference.md` → Phase 3: Validation; Phase 4: Output (pipeline hooks &
  story-link traceability)
- Checklists: `../forms.md` → Quality Checklist; Validation Criteria

## Team Integration

- **Product Planning Team** — as the quality gate ensuring story completeness before task
  generation
- Pairs well with: STORY-DECOMPOSE (produces what this sub-skill validates), a QA-strategy
  sub-skill (testing strategy depends on coverage validation)
