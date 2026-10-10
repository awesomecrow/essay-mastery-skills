#!/usr/bin/env python3
"""Zero-dependency standalone verification script for Essay Mastery.
Evaluates essay drafts directly using Python standard library heuristics across the 7 Levels of Resolution.
"""

import sys
import re
import math
import argparse
from pathlib import Path

# Common clutter phrases
CLUTTER_PHRASES = [
    r"\bin order to\b",
    r"\bdue to the fact that\b",
    r"\bat this point in time\b",
    r"\ba large number of\b",
    r"\ba majority of\b",
    r"\bfor the purpose of\b",
    r"\bwith regard to\b",
    r"\bit is important to note that\b",
]

# Nominalization suffixes
NOMINALIZATIONS = ("tion", "tions", "ment", "ments", "ance", "ances", "ence", "ences", "ity", "ities")

# Passive voice heuristic pattern
BE_FORMS = r"\b(am|is|are|was|were|be|been|being)\b"
PASSIVE_PATTERN = re.compile(rf"{BE_FORMS}\s+(?:\w+ly\s+)?([a-z]+(?:ed|en|wn|ne|pt))\b", re.IGNORECASE)


def count_syllables(word: str) -> int:
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 1
    if len(word) <= 3:
        return 1
    if word.endswith("e") and not word.endswith("le"):
        word = word[:-1]
    count = len(re.findall(r"[aeiouy]+", word))
    return max(1, count)


def audit_essay(text: str, target_words: int = None, is_rough: bool = False):
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("#")]
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip() and not s.strip().startswith("#")]
    words = re.findall(r"\b[A-Za-z0-9'-]+\b", text)

    total_words = len(words)
    total_sentences = len(sentences)
    total_paragraphs = len(paragraphs)
    total_syllables = sum(count_syllables(w) for w in words)

    if total_words == 0 or total_sentences == 0:
        return {"grade": "F", "words": 0, "issues": ["Document is empty."]}

    words_per_sent = total_words / total_sentences
    syllables_per_word = total_syllables / total_words
    reading_ease = 206.835 - (1.015 * words_per_sent) - (84.6 * syllables_per_word)
    fk_grade = (0.39 * words_per_sent) + (11.8 * syllables_per_word) - 15.59

    sent_lengths = [len(re.findall(r"\b[A-Za-z0-9'-]+\b", s)) for s in sentences]
    if len(sent_lengths) > 1:
        mean_len = sum(sent_lengths) / len(sent_lengths)
        variance = sum((l - mean_len) ** 2 for l in sent_lengths) / (len(sent_lengths) - 1)
        cadence_cv = math.sqrt(variance) / mean_len if mean_len > 0 else 0.0
    else:
        cadence_cv = 0.0

    # Passive voice count
    passives = sum(1 for s in sentences if PASSIVE_PATTERN.search(s))
    passive_pct = (passives / total_sentences) * 100

    # Nominalizations
    nominal_count = sum(1 for w in words if len(w) > 5 and any(w.lower().endswith(sfx) for sfx in NOMINALIZATIONS))
    nominal_pct = (nominal_count / total_words) * 100

    # Clutter phrases
    clutter_found = []
    for pattern in CLUTTER_PHRASES:
        m = re.findall(pattern, text, re.IGNORECASE)
        if m:
            clutter_found.extend(m)

    issues = []
    # L1: Clutter & Nominalizations
    if clutter_found:
        issues.append(f"Level 1: Found {len(clutter_found)} clutter phrase(s) (e.g. {clutter_found[0]}).")
    if nominal_pct > 6.0:
        issues.append(f"Level 1: High nominalization density ({nominal_pct:.1f}%). Replace abstract nouns with verbs.")

    # L2: Passive voice & Runaways
    if passive_pct > 18.0:
        issues.append(f"Level 2: Excessive passive voice ({passive_pct:.1f}%). Target < 15%.")
    runaways = sum(1 for l in sent_lengths if l > 38)
    if runaways > 0:
        issues.append(f"Level 2: {runaways} runaway sentence(s) exceeding 38 words detected.")

    # L3: Paragraph length
    for idx, p in enumerate(paragraphs, 1):
        pw = len(re.findall(r"\b[A-Za-z0-9'-]+\b", p))
        if pw > 250:
            issues.append(f"Level 3: Paragraph #{idx} exceeds 250 words ({pw} words). Split to maintain 1 premise per paragraph.")

    # L6: Cadence
    if cadence_cv < 0.35:
        issues.append(f"Level 6: Sentence cadence is monotone (CV: {cadence_cv:.2f} < 0.35). Alternate short and long sentences.")

    # Buffer checking
    if target_words:
        buffer_ratio = total_words / target_words
        if is_rough and buffer_ratio < 1.20:
            issues.append(f"Buffer Rule: Rough draft has only {buffer_ratio:.2f}x of target. Needs +25% surplus before pruning.")
        elif not is_rough and buffer_ratio > 1.10:
            issues.append(f"Length: Final draft is {buffer_ratio:.2f}x of target. Cut down to within 10% of target word count.")

    score = max(50, 100 - (len(issues) * 10))
    grade = "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "D"))

    return {
        "grade": grade,
        "score": score,
        "words": total_words,
        "sentences": total_sentences,
        "flesch_grade": round(fk_grade, 1),
        "cadence_cv": round(cadence_cv, 2),
        "passive_pct": round(passive_pct, 1),
        "issues": issues,
    }


def main():
    parser = argparse.ArgumentParser(description="Standalone zero-dependency verification for essay drafts.")
    parser.add_argument("file_path", type=Path, help="Path to markdown essay file")
    parser.add_argument("--target", type=int, default=None, help="Target final word count")
    parser.add_argument("--rough-draft", action="store_true", help="Check as rough draft (+25% buffer target)")
    args = parser.parse_args()

    if not args.file_path.exists():
        print(f"Error: File not found: {args.file_path}", file=sys.stderr)
        sys.exit(1)

    text = args.file_path.read_text(encoding="utf-8")
    report = audit_essay(text, target_words=args.target, is_rough=args.rough_draft)

    print(f"Audit Report: {args.file_path.name}")
    print(f"Overall Grade : {report['grade']} (Score: {report.get('score', 0)}/100)")
    print(f"Total Words   : {report['words']} words across {report.get('sentences', 0)} sentences")
    print(f"Flesch Grade  : {report.get('flesch_grade', 0.0)} (Cadence CV: {report.get('cadence_cv', 0.0)})")
    print(f"Passive Voice : {report.get('passive_pct', 0.0)}%")
    print(f"Issues Found  : {len(report['issues'])}")

    if report["issues"]:
        print("\nActionable Recommendations:")
        for idx, issue in enumerate(report["issues"], 1):
            print(f"  [{idx}] {issue}")
        sys.exit(0)
    else:
        print("\n[OK] No structural or stylistic violations detected. Exemplary rigor!")
        sys.exit(0)


if __name__ == "__main__":
    main()
