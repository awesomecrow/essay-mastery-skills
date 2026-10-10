---
name: essay-mastery
description: "End-to-end framework and deterministic workbench for formulating, structuring, expanding, and multi-resolution editing of essays based on the 10-step iterative method and 7 levels of resolution."
version: 1.0.0
triggers:
  - "write essay"
  - "draft essay"
  - "critique essay"
  - "outline essay"
  - "edit essay"
  - "refine essay"
  - "essay-mastery"
tags:
  - academic-writing
  - critical-thinking
  - rhetoric
  - editing
  - argument-architecture
---

# Essay Mastery Skill (`essay-mastery`)

## 1. System Philosophy & Purpose
Writing is an exercise in verbal thought and cognitive organization. The primary objective of an essay is not mechanical fulfillment of word requirements, but the formulation, defense, and refinement of an informed, coherent, and sophisticated argument.

An essay operates across **Seven Levels of Resolution simultaneously**:
1. **Level 1 - Word**: Precision, fitting connotation, active verbs, elimination of nominalizations.
2. **Level 2 - Sentence**: One clear proposition; brevity, rhythmic variation, and melodic cadence.
3. **Level 3 - Paragraph**: Single distinct thesis per paragraph (100-150 words / ~8 to 12 sentences).
4. **Level 4 - Paragraph Progression**: Coherent stepping-stones linking beginning to conclusion.
5. **Level 5 - The Essay as a Whole**: Overall vitality, originality, and intellectual rigor.
6. **Level 6 - The Reader**: Cognitive expectations, clarity, and steel-manning counterargument anticipation.
7. **Level 7 - Cultural/Disciplinary Context**: Foundational assumptions, definitions, and scholarly citation standards.

For deep guidance on resolution levels, consult [references/seven-levels-of-resolution.md](references/seven-levels-of-resolution.md).

---

## 2. Core Execution Protocol (10-Step Workflow)

The skill guides or executes the following steps sequentially or modularly:

```
[Phase 1: Inception]       Step 1: Topic Question formulation
                          Step 2: Source Curation & Gist Synthesis (Memory notes)
[Phase 2: Architecture]    Step 3: Primary Outline (10-15 sentences = the spine)
[Phase 3: Generation]      Step 4: Rough Draft Expansion (+25% length buffer target)
[Phase 4: Multi-Pass Edit] Step 5: Dual-Sentence Rewrite (15-25% reduction target)
                          Step 6: Sentence Sequencing within Paragraphs
                          Step 7: Paragraph Re-ordering & Logical Flow
[Phase 5: Distillation]    Step 8: Memory-Distillation Re-Outlining (blind reconstruct)
                          Step 9: Iterative Convergence (edit until delta is zero)
[Phase 6: Verification]    Step 10: Citation Integrity & Formatting (APA/target style)
```

For comprehensive procedural details, see [references/ten-step-methodology.md](references/ten-step-methodology.md).

---

## 3. Automated Verification Script

The skill includes a zero-dependency standalone verification script for testing essay drafts:

```bash
python scripts/verify_essay.py <file.md> [--target 1500] [--rough-draft]
```

It computes readability (Flesch Grade), sentence cadence variation ($CV \ge 0.35$), passive voice percentage, nominalization density, paragraph length boundaries, and buffer ratios.

---

## 4. Agent Guidelines for Antigravity & OpenCode

When acting as an essay writing assistant or authoring an essay:

1. **Phased Execution (Do Not Dump Monoliths):**
   * Never output an unprompted 2,000-word draft in a single turn. Always split into:
     - **Turn 1:** Topic question formulation + Fascination Audit.
     - **Turn 2:** 10-15 sentence Outline (the pure spine).
     - **Turn 3:** Rough draft expansion with deliberate surplus (+25% buffer target).
     - **Turn 4:** Dual-sentence revision and linter audit.
2. **Enforce the Dual-Sentence Trimming Rule:**
   * When editing, present the original sentence alongside a 15%-25% leaner rewrite with active verbs and zero fluff.
3. **Audit via the Verification Script:**
   * Run `python scripts/verify_essay.py <file>` to ensure the text satisfies quality standards before concluding.

---

## 5. References & Templates

- [Seven Levels of Resolution Guide](references/seven-levels-of-resolution.md)
- [Ten-Step Methodology Guide](references/ten-step-methodology.md)
- [Quality & Diagnostic Rubric](references/quality-rubric.md)
- [Citation Integrity Guide](references/citation-integrity.md)
- [Philosophical Argument Template](templates/philosophical_argument.md)
- [Empirical Scientific Template](templates/empirical_scientific.md)
- [Policy Brief Template](templates/policy_brief.md)
- [Personal Statement Template](templates/personal_statement.md)

