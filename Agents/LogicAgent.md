# LogicAgent — NordDRG Logic Benchmark

**What this is.** A lightweight, single-role agent that answers the **13 NordDRG Logic tasks (Logic-1–Logic-13)** using only the attached NordDRG artefacts — **no web access**.

**What’s included.** The agent ships with:
- **NordDRG Combined tables** workbook (consolidates **all national DRG versions**)
- Two official governance PDFs

This README exists to make setup **trivial** in commercial LLM tools (e.g., **OpenAI Assistants/GPTs**, **Anthropic Projects/Workflows**): upload the three artefacts as the agent’s context and use the system prompt below.

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

2. **Attach context (the three files below)**
   - Most platforms ignore folder paths after upload; keep filenames intact.
   - If your platform respects paths, use the **repo-root–relative** paths under **Context files**.

3. **Set the system prompt** (see **System prompt** below).

4. **Disable Web Searches** 
   - Turn off/bypass any *web browsing*, *search*, *RAG*, or *connector* tools in the UI.
   - Otherwise the agent might retrieve answers from the web, which violates the benchmark’s artefact-only constraint.

5. **Run Logic tasks (Logic-1–Logic-13)**  
   The agent answers strictly from the provided artefacts and returns **comma-separated, order-invariant lists**.

---

## Core capability

A single-role LogicAgent that reads the combined NordDRG tables and governance PDFs to answer the 13 Logic tasks deterministically from the source materials (no external tools or browsing).

**Benchmark description:** <https://arxiv.org/abs/2506.13790>

---

## Context files (relative to the Git repo root)

- [NordDRG_Documentation/How_to_read_NordDRG_definition_tables_2021-12-20.pdf](../NordDRG_Documentation/How_to_read_NordDRG_definition_tables_2021-12-20.pdf) 
- [NordDRG_Documentation/How_to_write_technical_changes_for_NordDRG_2021-12-21.pdf](../NordDRG_Documentation/How_to_write_technical_changes_for_NordDRG_2021-12-21.pdf) 
- [NordDRG_Combined2024PL/2023-06-14_Combined2024PL_xls.xlsx](../NordDRG_Combined2024PL/2023-06-14_Combined2024PL_xls.xlsx) — definition tables workbook containing all national DRG versions


---

## System prompt (for the Agent setup)

```text
Read the attached tables and PDF documents. Answer the following questions only based on the documents provided to you in this context. Do not use web searches.

Return results as comma-separated, order-invariant lists. Example: A, B, C

for binary tasks return exactly Yes or No
