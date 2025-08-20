# GrouperAgent — NordDRG Grouper Benchmark (Finland)

**What this is.** A lightweight, single-role agent that **emulates the official NordDRG grouper** for the 13 benchmark cases (Grouper-1–Grouper-13) using only the attached NordDRG artefacts — **no web access**.

**What’s included.** This agent is configured with the **NordDRG Finnish Definition tables** (FI national version only) and the two official governance PDFs.  
It is **designed for the Grouper benchmark only**.

> **Limitation:** Because this agent uses the **Finnish-only** workbook (not the multi-country “Combined” workbook), it **cannot** answer Logic tasks that require codes from other national versions. Use the LogicAgent with the Combined tables for cross-country Logic tasks.

---

## Why this setup (read me first)

This README is an **easy, no-code guideline** for setting up a working Grouper agent that:
1. **Requires no programming skills** — upload files, paste the system prompt, and run.
2. **Enables traceable reasoning** — capture an **audit/evidence trace** (e.g., `drg_logic.id`, evaluated predicates, and row references) explaining *why* a result was produced.  
   *Note:* this records verifiable evidence (tables/rows/conditions), **not** the model’s hidden chain-of-thought.
3. **Makes interaction simple** — use native chat-style UIs in OpenAI/Anthropic to run cases and ask follow-ups like “show the evidence trace.”
4. **Accounts for commercial tool limits** — instructions below explicitly **disable web/RAG** and keep context small enough to run under typical platform restrictions/quotas.

---

## Model compatibility (provider-agnostic)

This configuration is **LLM-agnostic** and works with any model available in commercial tools (OpenAI, Anthropic, Google, etc.) as long as the platform lets you upload files and disable web/RAG.

**Requirements**
- **File context**: The UI must support attaching the two PDFs and one Excel workbook as context/knowledge.
- **No external tools**: Disable browsing/search, code interpreters, function calling, databases, and connectors.
- **Sufficient context window**: Large enough to ingest the attached files. 

---

## Quick start (OpenAI / Anthropic)

1. **Create the agent**
   - OpenAI: create a GPT or Assistant.
   - Anthropic: create a Project/Workflow with a tool-free agent.

2. **Attach context (the files below)**
   - Most platforms ignore folder paths after upload; keep filenames intact.
   - If your platform respects paths, use the **repo-root–relative** paths under **Context files**.

3. **Set the system prompt** (see **System prompt** below).

4. **Disable Web Searches**
   - Turn off/bypass any *web browsing*, *search*, *RAG*, or *connector* tools in the UI.
   - Otherwise the agent might retrieve answers from the web, which violates the benchmark’s artefact-only constraint.

5. **Run Grouper tasks (Grouper-1–Grouper-13)**  
   The agent applies the governed control flow in `drg_logic` and returns exactly:  
   `drg_nat=<DRG>, drg_logic_id=<ID>`

> **Tip (evidence trace).** After getting an answer, you can ask:  
> “Show a concise **evidence trace** (sheet/row IDs and predicate outcomes only; no hidden reasoning).”

---

## Core capability

A single-role GrouperAgent that reads the **Finnish** Definition tables and governance PDFs to **reproduce the official grouping decision** for each structured test case by respecting: **`ORD` priority, age/sex bounds, MDC entry, OR/PROCPRO evidence, CC/MCC with exclusions, and national activation flags (Finland)**.

**Benchmark description:** <https://arxiv.org/abs/2506.13790>

---

## Context files (relative to the Git repo root)

- [NordDRG_Documentation/How_to_read_NordDRG_definition_tables_2021-12-20.pdf](../NordDRG_Documentation/How_to_read_NordDRG_definition_tables_2021-12-20.pdf) 
- [NordDRG_Documentation/How_to_write_technical_changes_for_NordDRG_2021-12-21.pdf](../NordDRG_Documentation/How_to_write_technical_changes_for_NordDRG_2021-12-21.pdf) 
- [NordDRG_FIN2026PL0/2024-04-15_FIN2026PL0_xlsx_wo_drgs.xlsx](../NordDRG_FIN2026PL0/2024-04-15_FIN2026PL0_xlsx_wo_drgs.xlsx) — definition tables workbook containing DRG grouper version for Finland

---

## System prompt (for the Agent setup)

```text
Read attached tables and PDF documents. Answer the following questions only based on the documents provided to you in this context. You are not allowed to use web searches.

Reproduce the official NordDRG grouping decision for the Finnish national version by applying the governed control flow over drg_logic.

Return exactly one line with two fields:
drg_nat=<DRG>, drg_logic_id=<ID>
