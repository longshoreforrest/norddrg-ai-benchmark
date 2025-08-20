# NordDRG‑AI Benchmark for Large‑Language Models

**Transparent, reproducible evaluation of Diagnosis‑Related Group (DRG) reasoning in modern LLMs**

---

## 🚀 Overview

This repository packages everything needed to reproduce the experiments described in our accompanying paper — *from raw NordDRG rule tables to a ready‑made prompt/answer set and evaluation scripts*.

The benchmark tests whether large‑language models can correctly reason over the complex classification logic used for hospital funding in the Nordic countries. It includes full DRG logic tables, governance manuals, and a set of 14 case-based tasks targeting code lookup, cross-table inference, and qualitative audits.

All artefacts are described in detail in the [arXiv paper (2025)](https://arxiv.org/abs/2506.13790).

---

## 📂 Repository layout

```text
├── Agents/
│   ├── LogicAgent.md                               # Documentation for Logic benchmark agent
│   └── GrouperAgent.md                             # Documentation for Grouper benchmark agent
│
├── NordDRG_Combined2024PL/                         # NordDRG Combined specification version for Logic tasks
│   ├── 2023-06-14_Combined2024PL_xls.xlsx          # Core logic and classification rules
│   ├── 2023-06-14_ICD+_NCSP+_Combined2024PL_xls.xlsx # ICD+NCSP links used in DRG assignments
│   ├── DRG_Names-FIN-Grouper-All-Names.xlsx        # All Finnish DRG names (multi-version)
│   ├── DRG_Names-FIN-Grouper-EN.xlsx               # English DRG names (subset)
│   ├── DRG_Names-FIN-Grouper-FI-EN.xlsx            # Bilingual Finnish–English names
│   └── DRG_Names-FIN-Grouper-FI.xlsx               # Finnish-only DRG names
│
├── NordDRG_Documentation/                          # Governance documentation
│   ├── How_to_read_NordDRG_definition_tables_2021-12-20.pdf
│   └── How_to_write_technical_changes_for_NordDRG_2021-12-21.pdf
│
├── NordDRG_FIN2026PL0/                             # NordDRG Finnish national version for Grouping tasks
│   └── 2024-04-15_FIN2026PL0_xlsx_wo_drgs.xlsx     # NordDRG Finnish national version
│
├── NordDRG_AI_Benchmark/                           # Benchmark resources
│   └── NordDRG Benchmark Questions and Answers - 2025-08-20.xlsx
│
├── README.MD                                       # Main repository readme
```

### Notes

* **Grouper specification versions** — Each folder like `NordDRG_Combined2024PL` corresponds to a specific DRG version. New versions (e.g. 2025, 2026) should be added in their own directories to preserve reproducibility across releases.
* **Benchmark Q\&A file** — `NordDRG Benchmark Questions and Answers – 2025-08-20.xlsx` includes prompts spanning both logic and grouping tasks, plus the gold-standard answer key in one consolidated Excel file.
* **PDF Manuals** — The two PDF documents explain how to read NordDRG definition tables and how to format technical change proposals, enabling evaluation of governance-aware model outputs.

---

## 📊 Evaluation Metrics

We report two official scores, matching the paper.

### 1) Logic suite — 13 rule-level tasks (Logic-1–Logic-13)
- **Metric:** macro-averaged **exact-match accuracy**.
- **What counts as correct:** your returned **set** of codes equals the gold set
  (case-insensitive, **order-invariant**, de-duplicated).
- **Binary items:** Logic-12/13 accept only `Yes` or `No`.

**Example (accepted):**
166N, 167X, 167O

### 2) Grouper suite — 13 case-level tasks (Grouper-1–Grouper-13)
- **Metric:** macro-averaged **strict exact-match accuracy**.
- **What counts as correct:** the answer must be **exactly one line** with **both** fields
  matching the gold pair:
drg_nat=<DRG>, drg_logic_id=<ID>

- Partial matches (e.g., correct `drg_nat` but wrong `drg_logic_id`) are scored **incorrect**.

**Example (accepted):**
drg_nat=470E, drg_logic_id=000D004100

---

## 🧪 Demonstration summary

A demonstration included in the preprint evaluates proprietary LLMs against the benchmark. Results confirm that the NordDRG benchmark captures cross-model variance invisible to general NLP leaderboards, especially on multilingual and governance-based tasks.

---

## 📝 Citation

If you use this benchmark, please cite:

```bibtex
@misc{pitkäranta2025norddrgaibenchmarklarge,
      title={The NordDRG AI Benchmark for Large Language Models}, 
      author={Tapio Pitkäranta},
      year={2025},
      eprint={2506.13790},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2506.13790}, 
}
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue before making major changes such as:

* Adding new question sets
* Supporting additional DRG versions
* Proposing alternative evaluation metrics

---

## ⚖️ License

All NordDRG tables are openly available through the NordDRG Forum:
https://nordcase.org/forum/
https://nordcaseforum.easyredmine.com/

A separate license document applies to the production of DRG Groupers and the use of national versions:
https://nordcase.org/products/groupers-definition-tables/

---

*Happy benchmarking!*
