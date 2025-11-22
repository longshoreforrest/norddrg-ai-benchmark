# Scripts

## Excel to CSV Conversion

The `run_conversion.py` script converts the NordDRG Excel file into individual CSV files.

### Usage

You can run the script from the project root or from the `scripts` directory.

**From project root:**
```bash
python3 scripts/run_conversion.py
```

**From scripts directory:**
```bash
cd scripts
python3 run_conversion.py
```

### Dependencies
Ensure you have the required dependencies installed (e.g., in a virtual environment):
```bash
pip install pandas openpyxl
```

## Benchmark Q&A Processing

The `process_benchmark_qa.py` script extracts questions and answers from the benchmark Excel file into categorized CSV files.

### Usage

```bash
python3 scripts/process_benchmark_qa.py
```

This will create the following files in `NordDRG_AI_Benchmark/CSV/`:
- `logic_questions.csv`
- `logic_answers.csv`
- `grouper_questions.csv`
- `grouper_answers.csv`

