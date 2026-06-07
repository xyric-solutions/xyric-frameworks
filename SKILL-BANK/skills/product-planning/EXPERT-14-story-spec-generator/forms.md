# Story Spec Generator — Templates & Checklists

Output templates, quality checklists, and validation criteria. Document locations and
filename shapes are organization-specific (see [`ADAPT.md`](ADAPT.md)); this file never
hardcodes them. The spec template content is platform-neutral and applies to any product.

---

## Workspace Intake (the questionnaire for adapting this skill)

Ask as one numbered list and **WAIT** for answers; then record them wherever your team
keeps workspace/naming decisions. Ask only what's missing.

1. **Products root** — where do per-product documents live (the root folder pattern, e.g. a products directory with one subfolder per product)?
2. **Doc areas** — within a product folder, where do stories, epic PRDs, the design system, specs, and the master requirements doc live (folder names)?
3. **Planning/status file** — what is the per-product planning/status filename you update with architecture decisions and milestones?
4. **Story ID convention** — how are story IDs formatted (e.g., epic.feature.sequence)?
5. **Spec filename convention** — how should the generated spec file be named (e.g., a per-story spec document)?
6. **Pipeline hook** — any marker convention you use to signal downstream tooling that a story is ready for task breakdown?

---

## Technical Specification Template

```markdown
# Technical Specification: [Story ID]
**[Story Title]**

---

## DOCUMENT INFORMATION

| Attribute | Value |
|-----------|-------|
| **Story ID** | S[XX.YY.ZZ] |
| **Story Title** | [Title] |
| **Epic/Feature** | E[XX] / F[X.Y] |
| **Version** | 1.0 |
| **Status** | Draft / Review / Approved |
| **Author** | [Name] |
| **Last Updated** | [Date] |

---

## 1. STORY REFERENCE

### User Story
**As a** [persona],
**I want to** [action],
**so that** [benefit].

### Acceptance Criteria
| ID | Criterion | Addressed In |
|----|-----------|--------------|
| AC1 | [Criterion 1] | API: `/endpoint`, UI: Component |
| AC2 | [Criterion 2] | Data: Entity, API: `/endpoint` |
| AC3 | [Criterion 3] | UI: Component, State: Store |

### Dependencies
- **Stories:** S[XX.YY.ZZ] (must complete first)
- **Features:** F[X.Y]
- **External:** [APIs, services]

---

## 2. TECHNICAL OVERVIEW

### Architecture Approach
[2-3 paragraphs describing the technical approach for this story]

### Architecture Alignment

| Aspect | Pattern | Rationale |
|--------|---------|-----------|
| Data Access | [Repository/Active Record/etc.] | [Why] |
| API Style | [REST/GraphQL/tRPC] | [Why] |
| UI Architecture | [Container-Presenter/Compound/etc.] | [Why] |
| State Management | [Local/Global/Server] | [Why] |

### Key Decisions

| Decision | Choice | Rationale | ADR Required? |
|----------|--------|-----------|---------------|
| [Decision 1] | [Choice] | [Why] | Yes / No |
| [Decision 2] | [Choice] | [Why] | No |

### ADR Flags (If Any)

**ADR Required:** [Decision Topic]
- **Impact:** High | Medium | Low
- **Scope:** Story | Epic | Product
- **Action:** Invoke the Software Architect skill for ADR creation
- **Context:** [Brief explanation]

### Component Diagram

```
[Frontend Component] --> [API Endpoint] --> [Database Table]
```

---

## 3. API CONTRACTS

### Endpoint: `[METHOD] /api/v1/[resource]`

**Purpose:** [What this endpoint does]
**Authentication:** Required / Optional / None
**Authorization:** [Role/permission required]

#### Request

```typescript
interface [RequestName]Request {
  field1: string;       // Description
  field2: number;       // Description
  field3?: boolean;     // Optional - Description
}
```

#### Response

```typescript
// Success Response (200/201)
interface [RequestName]Response {
  success: boolean;
  data: {
    id: string;
    field1: string;
    createdAt: string;  // ISO 8601
  };
}

// Error Response (4xx/5xx)
interface ErrorResponse {
  success: false;
  error: {
    code: string;       // e.g., "VALIDATION_ERROR"
    message: string;
    details?: object;
  };
}
```

#### Error Codes

| HTTP Status | Error Code | Description | User Message |
|-------------|------------|-------------|--------------|
| 400 | VALIDATION_ERROR | Invalid input | "Please check your input" |
| 401 | UNAUTHORIZED | Missing/invalid token | "Please sign in" |
| 403 | FORBIDDEN | Insufficient permissions | "You don't have access" |
| 404 | NOT_FOUND | Resource not found | "[Resource] not found" |
| 429 | RATE_LIMITED | Too many requests | "Please wait and try again" |
| 500 | INTERNAL_ERROR | Server error | "Something went wrong" |

---

## 4. DATA MODELS

### Entity: [EntityName]

```typescript
interface [EntityName] {
  id: string;                    // UUID v4
  field1: string;                // Description, constraints
  field2: number;                // Description, constraints
  field3: EntityStatus;          // Enum: ACTIVE | INACTIVE | PENDING
  relatedEntityId: string;       // FK to RelatedEntity
  createdAt: Date;
  updatedAt: Date;
  createdBy: string;             // FK to User
}
```

### Database Schema

```sql
CREATE TABLE [entity_name] (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  field1 VARCHAR(255) NOT NULL,
  field2 INTEGER NOT NULL DEFAULT 0,
  related_entity_id UUID REFERENCES related_entity(id),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_[entity]_field1 ON [entity_name](field1);
```

### Entity Relationships

```
[User] --1:N--> [Entity] --N:1--> [Related Entity]
```

### Migration Plan

| Step | Action | Rollback |
|------|--------|----------|
| 1 | Create table [entity] | Drop table |
| 2 | Add index idx_field1 | Drop index |
| 3 | Seed initial data | Delete seeded data |

---

## 5. UI COMPONENTS

### Component Hierarchy

```
[PageComponent]
+-- [HeaderComponent]
|   +-- [TitleComponent]
|   +-- [ActionsComponent]
+-- [ContentComponent]
|   +-- [ListComponent]
|   |   +-- [ItemComponent] (repeated)
|   +-- [EmptyStateComponent]
+-- [FooterComponent]
    +-- [PaginationComponent]
```

### Component: [ComponentName]

**Purpose:** [What this component does]

**Props:**
```typescript
interface [ComponentName]Props {
  data: DataType;
  onAction: (id: string) => void;
  isLoading?: boolean;
  errorMessage?: string;
  variant?: 'default' | 'compact' | 'expanded';
}
```

**State:**
```typescript
const [isOpen, setIsOpen] = useState(false);
const { data, isLoading, error } = useQuery(['key'], fetchFn);
```

**Events:**
| Event | Trigger | Handler |
|-------|---------|---------|
| onClick | User clicks [element] | handleClick |
| onSubmit | Form submission | handleSubmit |

**States:**
| State | Condition | Display |
|-------|-----------|---------|
| Loading | isLoading=true | Skeleton/Spinner |
| Error | error exists | Error message |
| Empty | data.length=0 | Empty state CTA |
| Success | data exists | Data display |

---

## 6. INTEGRATION POINTS

### Internal Integrations
| Integration | Type | Description |
|-------------|------|-------------|
| Auth Service | API | Token validation, user context |
| Notification Service | Event | Trigger notifications on [action] |

### External Integrations
| Integration | Type | Description | Failure Handling |
|-------------|------|-------------|------------------|
| [Third Party API] | REST | [Purpose] | [Fallback behavior] |

### Event Flows
```
User Action -> Component -> API -> Service -> Database
                                       |
                                 Event Bus -> Notification Service
```

---

## 7. SECURITY REQUIREMENTS

### Authentication
| Requirement | Implementation |
|-------------|----------------|
| Auth method | JWT / Session / API Key |
| Token storage | httpOnly cookie / localStorage |
| Token refresh | [Strategy] |

### Authorization
| Action | Required Role | Required Permission |
|--------|---------------|---------------------|
| View | Any authenticated | read:[resource] |
| Create | [Role] | create:[resource] |
| Update | Owner or Admin | update:[resource] |
| Delete | Admin only | delete:[resource] |

### Data Protection
| Data Type | Protection | Storage |
|-----------|------------|---------|
| PII | Encrypted at rest | Database |
| Passwords | bcrypt hash | Database |
| Tokens | Signed JWT | Cookie |

### Input Validation
| Field | Validation Rules |
|-------|------------------|
| email | Email format, max 255 chars |
| [field] | [Rules] |

---

## 8. TESTING STRATEGY

### Unit Tests
| Component/Function | Test Cases | Priority |
|--------------------|------------|----------|
| [ComponentName] | Renders correctly, handles click | High |
| [ServiceFunction] | Returns correct data, handles errors | High |

### Integration Tests
| Integration | Test Cases | Priority |
|-------------|------------|----------|
| API -> Database | CRUD operations | High |
| Component -> API | Data fetching, error handling | High |

### E2E Tests
| User Flow | Steps | Priority |
|-----------|-------|----------|
| [Flow 1] | 1. [Step], 2. [Step], 3. [Assert] | High |

### Test Data Requirements
| Data Type | Source | Refresh Frequency |
|-----------|--------|-------------------|
| Mock data | Fixtures | Per test |
| Seed data | Script | Per test suite |

---

## 9. PERFORMANCE REQUIREMENTS

### Response Time Targets
| Operation | Target | Measurement |
|-----------|--------|-------------|
| API response | < [X]ms | p95 latency |
| Page load | < [X]s | LCP |
| Interaction | < [X]ms | FID |

### Optimization Strategies
| Area | Strategy | Implementation |
|------|----------|----------------|
| API | Response caching | Cache headers, Redis |
| Database | Query optimization | Indexes, pagination |
| Frontend | Code splitting | Dynamic imports |

---

## 10. OPEN TECHNICAL DECISIONS

### Decision: [Decision Topic]
**Context:** [Why this decision is needed]

| Option | Pros | Cons |
|--------|------|------|
| Option A | [Pros] | [Cons] |
| Option B | [Pros] | [Cons] |

**Recommendation:** [Option X] because [rationale]
**Decision Needed By:** [Date/Milestone]

---

## ACCEPTANCE CRITERIA MAPPING

| Criterion | API | Data | UI | Test |
|-----------|-----|------|----|----- |
| AC1: [Criterion] | `/endpoint` | Entity | Component | Unit + E2E |
| AC2: [Criterion] | `/endpoint` | - | Component | Unit |

**Coverage:** 100% of acceptance criteria addressed

---

## DOCUMENT GOVERNANCE

### Related Documents
| Document | Location | Status |
|----------|----------|--------|
| Story | your stories area | Approved |
| Epic PRD | your epic-PRD area | Approved |
| Tasks | your tasks area | [Status] |

### Review Checklist
- [ ] Technical approach reviewed by architect
- [ ] Security review completed
- [ ] API contracts reviewed
- [ ] Test strategy approved
- [ ] Performance targets agreed

---

*Technical Specification v1.0 | Story [ID] | [Product Name] | [Date]*

<!-- TASKS_READY: S[XX.YY.ZZ] -->
```

---

## Quality Checklist

### Section Completeness
- [ ] Story Reference (user story, criteria, dependencies)
- [ ] Technical Overview (approach, decisions, diagram)
- [ ] API Contracts (endpoints, schemas, errors)
- [ ] Data Models (entities, schema, relationships)
- [ ] UI Components (hierarchy, props, state, events)
- [ ] Integration Points (internal, external, events)
- [ ] Security Requirements (auth, authz, data protection)
- [ ] Testing Strategy (unit, integration, e2e)
- [ ] Performance Requirements (targets, limits, optimization)
- [ ] Open Technical Decisions (options, recommendations)

### Coverage Checks
- [ ] Every acceptance criterion addressed
- [ ] All APIs have request/response schemas
- [ ] All entities have field definitions
- [ ] All components have props/state defined
- [ ] Test strategy covers all layers

### Quality Standards
- [ ] No TBD or placeholder content
- [ ] Response time targets are numbers
- [ ] Error codes are specific
- [ ] Security requirements are actionable
- [ ] Test cases are specific

---

## Activation Checklist

When this skill is activated:

**Phase 0: Research**
1. [ ] Identify target story (per your story ID convention)
2. [ ] Read the story from your stories area
3. [ ] Read the Epic PRD for feature context
4. [ ] Read the design system for patterns
5. [ ] Generate Story Technical Context (~300 words)

**Phase 1: Analysis**
6. [ ] Present context to the user
7. [ ] Ask 5 tailored technical questions
8. [ ] **WAIT for user responses**
9. [ ] (Optional) Ask follow-up questions if needed

**Phase 2: Generation**
10. [ ] Apply user decisions
11. [ ] Generate all 10 sections sequentially
12. [ ] Ensure acceptance criteria addressed
13. [ ] Build criteria mapping

**Phase 3: Validation (Blocking)**
14. [ ] Verify all acceptance criteria mapped
15. [ ] Verify all sections present
16. [ ] Verify no placeholder content
17. [ ] If fails → return to Phase 2 and fix

**Phase 4: Output**
18. [ ] Write the spec to your specs area, named per your spec filename convention
19. [ ] Update your planning/status file
20. [ ] Include the pipeline hook for the Task Generator
21. [ ] Present completion summary

---

*Forms | Story Spec Generator | community template*
