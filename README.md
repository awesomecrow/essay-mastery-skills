# Essay Mastery Skill (`essay-mastery`)

> **End-to-end agent skill framework for formulating, structuring, expanding, and multi-resolution editing of essays based on the 10-Step Writing Methodology and 7 Levels of Resolution.**

---

## Overview

This repository contains the pure, self-contained **Essay Mastery Agent Skill** designed for AI coding assistants and agent environments (such as Antigravity, OpenCode, and Codex).

It replaces mechanical, superficial text generation with cognitive and rhetorical rigor:
- **10-Step Iterative Protocol:** From topic question calibration to blind memory re-outlining.
- **7 Levels of Resolution:** Simultaneous evaluation across words, sentences, paragraphs, chapter progressions, macro structure, cadence, and citation integrity.
- **Zero-Dependency Verification Script:** Standalone Python script (`scripts/verify_essay.py`) to audit Flesch readability, sentence cadence variation, passive voice, nominalizations, and word count buffer ratios.

---

## Repository Structure

```
essay-mastery/
├── SKILL.md                          # Main agent instructions & progressive disclosure
├── README.md                         # Repository documentation
├── scripts/
│   └── verify_essay.py               # Standalone zero-dependency essay draft auditor
├── references/
│   ├── seven-levels-of-resolution.md # Deep specifications for L1 through L7
│   ├── ten-step-methodology.md       # Procedural guide for Steps 1 through 10
│   ├── quality-rubric.md             # Rigor standards, grades, and failure modes
│   └── citation-integrity.md         # Source verification and citation guidelines
└── templates/
    ├── philosophical_argument.md     # Dialectical thesis-antithesis-synthesis structure
    ├── empirical_scientific.md       # IMRAD empirical structure
    ├── policy_brief.md               # Executive summary and recommendation structure
    └── personal_statement.md         # Narrative arc and reflection structure
```

---

## Installation & Skill Registration

### 1. Antigravity / Agent Skills CLI

To install or register this skill in your agent environment:

**Via global skills directory:**
Clone or copy this repository to your global skills path:
```bash
# Windows
git clone https://github.com/your-username/essay-mastery.git "$HOME\.agents\skills\essay-mastery"

# Linux / macOS
git clone https://github.com/your-username/essay-mastery.git "$HOME/.agents/skills/essay-mastery"
```

Once placed in `~/.agents/skills/essay-mastery`, any agent session with agent skills capability will automatically discover and trigger `essay-mastery`.

---

## How to Use With Your AI Assistant

You do not need to install complex software or run local terminal TUIs. Simply talk to your AI agent with prompts such as:

### 1. Topic Calibration & Fascination Audit
> *"I want to write an essay on cognitive attention in modern technology. Activate the essay-mastery skill and run Step 1 (Topic Question Formulation & Fascination Audit) with me."*

### 2. 10–15 Sentence Outline (The Spine)
> *"Based on our topic question, construct the primary outline (Step 3: The Spine) consisting of 12 distinct propositional sentences."*

### 3. Expansion (+25% Buffer)
> *"Draft the rough expansion for section 2. Maintain a +25% word surplus buffer so we have enough material to prune during revision."*

### 4. Dual-Sentence Rewrite Audit (Step 5)
> *"Perform a dual-sentence rewrite audit on this paragraph. For each sentence, provide Option A (lean compression) and Option B (rhetorical punch) targeting a 15-25% reduction in filler words."*

### 5. Automated Quality Check (Local Python)
You can run the zero-dependency verification script at any time:
```bash
python scripts/verify_essay.py path/to/draft.md --target 1500
```

---

## License

MIT License.
