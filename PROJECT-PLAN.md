# PROJECT-PLAN.md — ODR Thesis: The Compton Count as Primitive

**Project Slug:** `odr-thesis`
**Phase:** 4 (Deep Research — post red-team v1 remediation)
**Date:** 2026-08-03

---

## Charter

**Mission:** Produce a single, definitive synthesis paper that unifies all five ODR research questions (RQ1–RQ5) into a coherent thesis: *physics runs on \(\mathbb{Q}\), not \(\mathbb{R}\); the Bruhat–Tits tree is the coordinate system; the Compton count is the only primitive.*

**Scope:** A peer-review–ready preprint (target: 25-40 pages, ~40-60 references) with a structured abstract, five body sections (one per RQ), a synthesis conclusion, and a falsifiability register.

**Out of Scope:** Experimental design beyond falsifiability conditions; full numerical computation of BT-tree scattering amplitudes (those are RQ4 sub-projects); novel condensed matter derivations (already in quasiparticle extension paper).

---

## Work Breakdown Structure

### Phase 0: Project Initialization
| ID | Task | Status |
|:---|:-----|:-------|
| P0.1 | Scaffold directories + git init | COMPLETE (v0.1-phase0) |
| P0.2 | README.md | COMPLETE |
| P0.3 | PROJECT-PLAN.md | COMPLETE |
| P0.4 | .gitignore | COMPLETE |
| P0.5 | Core claim lock | COMPLETE |
| P0.6 | Git commit + tag v0.1-phase0 + push | COMPLETE |
| P0.7 | KG entry | COMPLETE |

### Phase 1: Due Diligence
| ID | Task | Status |
|:---|:-----|:-------|
| P1.1 | QNFO cross-reference (KG + D1 + Vectorize) | COMPLETE (v0.2-phase1-dd) |
| P1.2 | External literature search (8 sources) | COMPLETE |
| P1.3 | Gap analysis | COMPLETE |
| P1.4 | Consilience Gate (KIF-29, HARD) | COMPLETE |

### Phase 2: Literature Search & Triage
| ID | Task | Status |
|:---|:-----|:-------|
| P2.1 | Multi-source search (parallel) | COMPLETE (v0.3-phase2-lit) |
| P2.2 | Classification matrix (Core/Supporting/Background/Reject) | COMPLETE |
| P2.3 | Mandatory Symmetry Template (KIF-18) | COMPLETE |

### Phase 3: Citation Management
| ID | Task | Status |
|:---|:-----|:-------|
| P3.1 | Extract citations from draft | COMPLETE (v0.4-phase3-cite) |
| P3.2 | Verify BibTeX entries | COMPLETE — **RED-TEAM CORRECTED v1: 28 unique entries, all 19 DOIs verified via Crossref/DataCite (v0.5-redteam-fix)** |
| P3.3 | Auto-generate missing DOIs | COMPLETE (manual construction documented — DOI→BibTeX endpoint returns HTML redirects; entries built from Crossref/OpenAlex metadata) |

### Phase 4: Deep Research & Structured Forecast
| ID | Task | Status |
|:---|:-----|:-------|
| P4.1 | Domain Assessment | IN PROGRESS |
| P4.2 | Paradigm-Shift Candidates | PENDING |
| P4.3 | Assumption Audit | PENDING |
| P4.4 | Red-Team Challenge (5 adversary) | PENDING |
| P4.5 | Calibration Register | PENDING |
| P4.6 | Practical Applications Extension | PENDING |
| P4.7 | Counterfactual Backcasting | PENDING |

### Phase 5: Publication Pipeline
| ID | Task | Status |
|:---|:-----|:-------|
| P5.1 | Draft paper (5 RQ sections + synthesis) | PENDING |
| P5.2 | BP gates (BP-1 through BP-10) | PENDING |
| P5.3 | Certainty calibration pass | PENDING |
| P5.4 | Banned words scan | PENDING |
| P5.5 | Mojibake scan | PENDING |
| P5.6 | PDF build (pandoc→xhtml2pdf fallback) | PENDING |
| P5.7 | Zenodo upload with DOI | PENDING (R1: token 403 — needs deposit:write scope) |

### Phase 6: Cloudflare Deployment
| ID | Task | Status |
|:---|:-----|:-------|
| P6.1 | D1 living-paper insert | PENDING |
| P6.2 | Papers-server verification | PENDING |
| P6.3 | R2 archive | PENDING |

### Phase 7: Dissemination
| ID | Task | Status |
|:---|:-----|:-------|
| P7.1 | SEO audit | PENDING |
| P7.2 | Social media (Buffer) | PENDING |
| P7.3 | Internet Archive | PENDING |

### Phase 8: Core Distribution
| ID | Task | Status |
|:---|:-----|:-------|
| P8.1 | GitHub push + release tag | PENDING |
| P8.2 | Zenodo newversion (if applicable) | PENDING |
| P8.3 | D1/KG records update | PENDING |

---

## Milestones

| Milestone | Gate | Target Date | Status |
|:----------|:-----|:------------|:-------|
| M0: Phase 0 Complete | Repo initialized, pushed, tagged, KG entry | 2026-08-03 | DONE |
| M1: Due Diligence Complete | Consilience Gate passed, literature classified | 2026-08-03 | DONE |
| M2: Deep Research Complete | Forecast report + calibration register | 2026-08-04 | IN PROGRESS |
| M3: Draft Complete | Full paper with all 5 RQ sections | 2026-08-05 | PENDING |
| M4: Publication Complete | PDF built, BPs passed, Zenodo DOI | 2026-08-06 | PENDING |
| M5: Distribution Complete | D1, R2, papers-server, GitHub release | 2026-08-07 | PENDING |

---

## Deliverable Registry

| ID | Deliverable | Format | Destination |
|:---|:------------|:-------|:------------|
| D0 | PROJECT-PLAN.md | Markdown | repo root |
| D1 | Due Diligence Report | Markdown | artifacts/due-diligence.md |
| D2 | Consilience Gate | Markdown | artifacts/consilience-gate.md |
| D3 | Literature Search Evidence | JSON + Markdown | artifacts/external-search/ |
| D4 | Structured Forecast Report | Markdown | artifacts/structured-forecast.md |
| D5 | Red-Team Audit | Markdown | artifacts/red-team-audit.md |
| D6 | Final Paper | Markdown + PDF | releases/odr-thesis-v1.0.pdf |
| D7 | Zenodo DOI | Web | doi.org/10.5281/zenodo/XXXXX |
| D8 | D1 Paper Record | SQL | QNFO D1 database |

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|:---|:-----|:----------|:-------|:-----------|
| R1 | Zenodo 403 (token scope) | HIGH | BLOCK | Regenerate token with deposit:write |
| R2 | RQ3 (BT coordinates) insufficiently formalized | MODERATE | HIGH | Scope as "proposal sketch" rather than full derivation |
| R3 | RQ4 (testable prediction) too weak to satisfy skeptical reviewer | HIGH | MODERATE | Include at least one concrete numerical prediction |
| R4 | 5-RQ synthesis becomes unfocused / each section too shallow | MODERATE | HIGH | Strict page budget per RQ; cross-refer to existing papers |
| R5 | RQ2 (Q vs R) requires novel mathematics not yet developed | MODERATE | MODERATE | Cite Continuum Trilogy; state open problems explicitly |

---

## Success Criteria

1. All 5 RQs addressed in a single, coherent paper
2. Consilience Gate passed (KIF-29 HARD)
3. At least one falsifiable prediction per speculative RQ (RQ1–RQ4)
4. PDF built and verified (zero U+FFFD)
5. Zenodo DOI obtained
6. All compliance gates passed (mojibake, banned words, certainty calibration, Ostrowski dimensionless)
