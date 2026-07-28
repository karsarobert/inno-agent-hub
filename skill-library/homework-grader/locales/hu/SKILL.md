---
name: homework-grader
category: Oktatás és tutorálás
version: 1.0.0
allowed-tools:
- Read
- Write
- Edit
- Bash
- Glob
- Grep
- Task
- WebFetch
tags:
- education
- grading
- evaluation
- rubric
- batch-processing
- quality-control
related:
- advanced-evaluation
- rubric
- content-evaluation-framework
templates:
- templates/rubric.yaml.tmpl
- templates/scoring-prompt.md
- templates/comment-generation-prompt.md
- templates/gate-check-prompt.md
- templates/calibration-report.md
- templates/scoring-output-schema.json
- templates/ir-schema.json
description: >-
  Rubrika-alapú AI házi feladat értékelő rendszer: szubjektív feladatok értékelése rubrika szerint, támogatja szöveges, képi és vegyes benyújtást, kötegelt feldolgozás; az értékelés bizonyítékokra hivatkozik, beépített PDCA minőségügyi ciklussal, egyéni visszajelzést generál, és képes az AI értékelés tanári mintákkal való konzisztencia-kalibrálására (Cohen κ / Spearman ρ / MAD), eredmények Excel-be exportálhatók.
  Rubrika-alapú AI házi feladat értékelő rendszer: szubjektív feladatok értékelése rubrika szerint, támogatja szöveges, képi és vegyes benyújtást, kötegelt feldolgozás; az értékelés bizonyítékokra hivatkozik, beépített PDCA minőségügyi ciklussal, egyéni visszajelzést generál, és képes az AI értékelés tanári mintákkal való konzisztencia-kalibrálására (Cohen κ / Spearman ρ / MAD), eredmények Excel-be exportálhatók.
---

# Homework Grader

A course-agnostic, Rubric-driven evaluation engine for grading student homework
with Claude. All course-specific knowledge lives in user-defined Rubric YAML
files; this Skill provides the scoring methodology, quality control framework,
and batch processing pipeline.

---

## When to Activate

Activate this Skill when the user:

- Asks to **grade**, **score**, or **evaluate** student homework or assignments
- Wants to **create a rubric** or **scoring criteria** for coursework
- Needs to **batch-process** a set of student submissions
- Asks about **calibrating** AI scoring against teacher standards
- Wants to **export grades** to Excel or generate **grade reports**
- Mentions **PDCA**, **quality control**, or **bias checking** in grading context
- References **homework**, **assignment**, **submission**, **coursework** evaluation

**Keywords**: grade homework, score assignments, rubric, evaluate student work,
batch grading, calibrate scoring, export grades, feedback comments, PDCA cycle

---

## Core Concepts

### Rubric-Driven Design

Every scoring decision traces back to a Rubric YAML file that defines:
- **Criteria** with weights, 1-5 anchors, and evidence types
- **Gates** for pre-scoring validation (keyword, structure, length, custom)
- **Thresholds** for accept/review/reject classification
- **Comment guidelines** for feedback language, tone, and structure

The Skill never invents criteria. If the Rubric doesn't define it, it doesn't
get scored.

### Direct Scoring Method

Each submission is scored independently against absolute standards (not compared
to peers). This is the correct method when objective criteria exist — which
Rubrics provide by definition.

- **Scale**: 1-5 Likert (integer scores per dimension)
- **Process**: Evidence → Reasoning → Score (never reversed)
- **Aggregation**: Weighted sum across dimensions

### PDCA Quality Cycle

Every grading batch follows Plan → Do → Check → Act:
- **Plan**: Define/validate Rubric, prepare calibration samples
- **Do**: Preprocess submissions, run AI scoring, generate comments
- **Check**: Calibrate against teacher scores, check distributions, detect bias
- **Act**: Human review of flagged items, refine Rubric for next round

### Multimodal Support

Submissions are preprocessed into a unified Intermediate Representation (IR)
before scoring. Supported modalities:
- **Text** (P0): docx, pdf → Markdown text
- **Image** (P1): jpg, png → Claude Vision structured descriptions
- **Video** (V2): mp4 → keyframes + transcript (future)
- **Mixed**: Combination of above

---

## PDCA Workflow

### Phase 1: Plan

**Goal**: Establish scoring standards and validation baseline.

| Step | Action | Output | Exit Criterion |
|------|--------|--------|----------------|
| 1.1 | Define or load Rubric YAML | `rubric.yaml` | Passes schema validation |
| 1.2 | Validate Rubric | Validation report | Weights sum to 1.0, anchors complete, gates well-formed |
| 1.3 | Prepare calibration samples | 3-5 teacher-scored samples | Cover good/medium/poor range |
| 1.4 | Configure batch parameters | Processing config | Submission format, batch size, mode |

**Exit**: Rubric validated + calibration samples ready + teacher confirms.

**Failure**: Invalid Rubric → fix and re-validate. No calibration samples →
teacher must provide at least 3 before proceeding to Do phase.

### Phase 2: Do

**Goal**: Process all submissions and produce AI scores.

| Step | Action | Output | Exit Criterion |
|------|--------|--------|----------------|
| 2.1 | Collect submissions | `workspace/raw/` | All files present and readable |
| 2.2 | Preprocess → IR | `workspace/ir/` | Each submission has valid IR JSON |
| 2.3 | Run gate checks | Gate results in IR | All gates executed, failures recorded |
| 2.4 | Score each submission | `workspace/scores/` | Each has dimension scores + comment |
| 2.5 | Generate comments | Comments in score records | 200-400 chars, three sections |

**Exit**: All submissions scored (or failed items logged).

**Failure**: API errors → retry with exponential backoff (max 3). File
corruption → log and skip. Parse errors → retry up to 2 times, then flag for manual.

### Phase 3: Check

**Goal**: Validate AI scoring quality.

| Step | Action | Threshold | On Failure |
|------|--------|-----------|------------|
| 3.1 | Calibration: AI vs teacher on samples | κ ≥ 0.70, ρ ≥ 0.80 per dimension | → Back to Plan: adjust anchors |
| 3.2 | Distribution check | \|skewness\| < 1.0, no >40% concentration | → Spot-check extreme scores |
| 3.3 | Bias detection | Length-score \|ρ\| < 0.3, position-score \|ρ\| < 0.2 | → Adjust prompts, re-score |
| 3.4 | Confidence filtering | ≤20% mandatory review (conf < 0.6) | → Review flagged items |

**Exit**: All checks pass, or teacher accepts results after reviewing issues.

**Failure**: κ < 0.70 → return to Plan phase, revise Rubric anchors.
Significant bias → adjust scoring prompts and re-run Do phase.

### Phase 4: Act

**Goal**: Finalize grades and capture lessons.

| Step | Action | Output |
|------|--------|--------|
| 4.1 | Human review of flagged items | Corrected scores |
| 4.2 | Export to Excel | Grade spreadsheet |
| 4.3 | Record Rubric adjustments (if any) | Updated Rubric version |
| 4.4 | Log lessons learned | Improvement log for next cycle |

**Exit**: Final grades exported + Rubric version updated if changed.

---

## Rubric Schema

A Rubric is a YAML file with the following structure. See
`templates/rubric.yaml.tmpl` for a copy-paste template.

### Required Fields

```yaml
rubric:
  id: "course-assignment-v1.0"       # Unique identifier
  name: "Human-readable name"
  version: 1.0

  criteria:
    criterion_id:
      name: "Dimension Name"
      weight: 0.30                    # All weights MUST sum to 1.0
      scale: [1, 2, 3, 4, 5]
      description: "What this measures"
      scoring_guidance: "How to evaluate"
      anchors:
        5: "Excellent — observable criteria"
        4: "Good — observable criteria"
        3: "Adequate — observable criteria"
        2: "Below average — observable criteria"
        1: "Poor — observable criteria"
      evidence_type: quote            # quote | observation | metric

  thresholds:
    accept: 3.0
    reject: 1.5
    review: [1.5, 3.0]               # Must equal [reject, accept]
```

### Optional Fields

> **Tip**: The `templates/rubric.yaml.tmpl` template includes additional
> optional fields (`created`, `updated`, `author`, `course.code`,
> `course.semester`, `gate.description`, `notes`) not listed here. They are
> informational metadata — the scoring engine ignores them, but they help
> with Rubric management.

```yaml
  course:                             # Remove entirely if not needed
    name: "Course Name"
    submission_type: text             # text | image | video | mixed
    expected_formats: [docx, pdf]
    student_count: 100

  gates:                              # Pre-scoring checks
    - id: "G-001"
      name: "Gate Name"
      check_method: keyword           # keyword | structure | length | custom
      parameters: { keywords: [...], min_count: 1 }
      on_fail: flag                   # fail | flag | warn

  comment_guidelines:
    tone: "constructive, specific"
    language: "zh-CN"
    length_range: [200, 400]
    required_sections: [strengths, weaknesses, suggestions]
    prohibited_patterns: [...]

  history:
    - version: 1.0
      date: "2026-01-01"
      changes: ["Initial version"]
```

### Validation Rules

| Rule | Check |
|------|-------|
| Weights | `sum(criteria.*.weight)` = 1.0 (±0.001) |
| Anchors | Every value in `scale` has an anchor description |
| Thresholds | `accept > reject`; `review = [reject, accept]` |
| Gate IDs | Unique within the Rubric |
| Gate on_fail | One of: `fail`, `flag`, `warn` |
| evidence_type | One of: `quote`, `observation`, `metric` |

---

## Scoring Protocol

This is the complete protocol for scoring a single submission. Claude executes
this directly — no external scripts required.

### Step 1: Load Rubric

Read the Rubric YAML. Validate structure. Extract criteria, gates, thresholds,
and comment guidelines.

### Step 2: Gate Checks

Execute each gate in order:

- **keyword**: Search submission text for `parameters.keywords`. Pass if
  `≥ min_count` distinct keywords found.
- **structure**: Check for `required_sections` (heading match) or
  `required_files` (glob match). Pass if all present.
- **length**: Count words (whitespace-separated for alphabetic languages) or
  characters (for CJK). Pass if within `[min_words, max_words]`.
- **custom**: Use LLM to evaluate `parameters.prompt` against submission.

Gate results:
- `on_fail: fail` → Record reason, **skip scoring entirely**
- `on_fail: flag` → Record warning, continue scoring
- `on_fail: warn` → Note for comment, continue scoring

### Step 3: Per-Dimension Scoring (CoT Required)

For **each** criterion in the Rubric, independently:

1. **Find Evidence**: Quote directly from the submission (if `evidence_type:
   quote`) or describe an observation. If no relevant content exists, state
   "No relevant evidence found."

2. **Reason Against Anchors**: Compare the evidence to each anchor description.
   Identify which level it matches. Explain why it doesn't meet the next level
   up. Note borderline cases.

3. **Assign Score**: Integer 1-5. Must follow from the reasoning — never
   assigned first.

4. **Suggest Improvement**: One specific, actionable suggestion for this
   dimension.

5. **Rate Confidence**: Float 0.0-1.0 based on:
   - Clarity of anchor match (clear → higher)
   - Sufficiency of evidence (more → higher)
   - Borderline ambiguity (ambiguous → lower)

### Anti-Bias Rules (Enforced During Scoring)

These rules are **mandatory** in every scoring interaction:

> **Length ≠ Quality**: Do NOT award higher scores because a submission is long.
> Concise, well-argued work is equal to or better than verbose work. Irrelevant
> padding should lower scores.
>
> **Tone ≠ Accuracy**: Do NOT assume confident language means correct content.
> Evidence-backed hedging outranks unsupported assertions.
>
> **Relevance Filter**: Only content relevant to the current dimension counts.
> Off-topic elaboration earns zero credit for that dimension.
>
> **Evidence Before Score**: Always find evidence first, reason second, score
> third. Reversing this order is forbidden.
>
> **Independent Dimensions**: Each dimension is scored on its own merits. A
> high score on one dimension must not inflate another.

### Step 4: Aggregate

```
weighted_total = Σ(criterion.weight × criterion.score)  # Round to 2 decimals
percentile     = round((weighted_total - 1) / 4 * 60 + 40)  # Maps 1→40, 5→100
overall_confidence = mean(per_dimension_confidence)
```

Grade classification (workflow routing — determines review queue):
- `weighted_total ≥ thresholds.accept` → **accept**
- `weighted_total < thresholds.reject` → **reject**
- Otherwise → **review**

> **Note**: This accept/review/reject classification is a **workflow** label that
> drives the PDCA Check and Act phases (which submissions need teacher review).
> It is separate from the **academic grade** (kiváló/jó/közepes/eltelt/gyenge) which is
> derived from the percentile score and appears in the Excel export. Both are
> computed from `weighted_total` but serve different purposes.

### Step 5: Generate Comment

Using the scoring results, generate a structured comment following
`comment_guidelines`:

- **Strengths**: 1-2 best dimensions, with evidence citations
- **Weaknesses**: 1-2 lowest dimensions, with specific gap description
- **Suggestions**: 2-3 prioritized, actionable improvements

Comment must be in the language specified by `comment_guidelines.language`.
Length must be within `comment_guidelines.length_range`.

### Step 6: Output

Produce a JSON record conforming to `templates/scoring-output-schema.json`.

---

## Scoring Prompt (Inline)

When Claude scores a submission, use this prompt structure. This is inlined
here so Claude can execute scoring without reading additional files.

### System Message

```
You are a meticulous homework evaluator. You score student submissions strictly
according to the provided Rubric. You never invent criteria beyond what the
Rubric defines.

Anti-Bias Directives:
1. Length ≠ Quality — Do NOT award higher scores for longer submissions.
   Irrelevant padding should lower scores.
2. Tone ≠ Accuracy — Do NOT assume confident language is correct.
   Evaluate claims against evidence.
3. Relevance filter — Only content relevant to the criterion counts.
4. Evidence before score — Quote/observe first, reason second, score third.
5. Independent dimensions — Score each dimension on its own merits.
```

### User Message Structure

```
## Rubric
[Insert full criteria with names, weights, anchors, scoring_guidance]

## Student Submission
[Insert IR content]

## Instructions
For each dimension:
1. Evidence — Quote or describe from submission
2. Reasoning — Compare against anchors, explain level match
3. Score — Integer 1-5
4. Improvement — One specific suggestion
5. Confidence — Float 0.0-1.0

Then:
6. Weighted Total — Σ(weight × score), 2 decimal places
7. Overall Confidence — Mean of dimension confidences

Output JSON only (no markdown fences):
{
  "student_id": "...",
  "rubric_id": "...",
  "dimension_scores": [
    {
      "criterion_id": "...",
      "criterion_name": "...",
      "weight": 0.0,
      "score": 0,
      "evidence": "...",
      "reasoning": "...",
      "improvement": "...",
      "confidence": 0.0
    }
  ],
  "weighted_total": 0.0,
  "overall_confidence": 0.0
}
```

---

## Comment Generation Prompt (Inline)

After scoring, generate the student-facing comment:

### System Message

```
You are a constructive academic mentor writing feedback. Your comments must be
specific, evidence-based, and actionable.

Rules:
- Three sections: strengths, weaknesses, suggestions
- No vague praise ("jól megírtad" without specifics is forbidden)
- No vague criticism ("erősíteni kell" without specifics is forbidden)
- Every remark must cite specific content from the submission
- Suggestions must be actionable (student knows exactly what to do)
- Length: per comment_guidelines.length_range
- Tone: per comment_guidelines.tone
- Language: per comment_guidelines.language
```

### User Message Structure

```
## Scoring Results
[Per-dimension scores, evidence, reasoning, improvements]

## Task
Write a comment with:
- [Strengths]: Best 1-2 dimensions with evidence
- [Weaknesses]: Lowest 1-2 dimensions with gap description
- [Suggestions]: 2-3 prioritized actions

Output JSON:
{
  "strengths": "...",
  "weaknesses": "...",
  "suggestions": "...",
  "full_text": "... (combined natural-language comment)"
}
```

---

## Quality Control Summary

### Three-Layer Architecture

| Layer | When | What | Tools |
|-------|------|------|-------|
| **L1: Gate QC** | Before scoring | File integrity, format, content gates | Gate checks in Rubric |
| **L2: Scoring QC** | During scoring | CoT enforcement, evidence requirement, anti-bias prompts | Built into scoring prompt |
| **L3: Audit QC** | After batch | Calibration, distribution, bias, confidence | `scripts/calibrate.py`, `scripts/stats.py` |

### Calibration Protocol

1. Teacher provides 3-5 scored samples (covering good/medium/poor)
2. AI scores the same samples independently
3. Calculate agreement metrics:
   - **Weighted Cohen's κ** ≥ 0.70 (overall agreement)
   - **Spearman ρ** ≥ 0.80 per dimension (ranking consistency)
   - **MAD** ≤ 0.5 (mean absolute difference — systematic drift)
4. If passing → proceed. If failing → adjust Rubric anchors and re-calibrate.

### Confidence Filtering

| Confidence | Action |
|------------|--------|
| ≥ 0.8 | Trusted — no review needed |
| 0.6 – 0.8 | Suggested review — spot-check recommended |
| < 0.6 | Required review — must be checked by teacher |

**Target**: ≤ 20% of submissions flagged for mandatory review (confidence < 0.6).

### Bias Monitoring (Post-Batch)
