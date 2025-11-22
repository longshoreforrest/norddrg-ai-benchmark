import pandas as pd
from pathlib import Path
import sys

def process_benchmark_qa():
    # Define paths
    project_root = Path(__file__).resolve().parent.parent
    input_file = project_root / "NordDRG_AI_Benchmark" / "NordDRG Benchmark Questions and Answers - 2025-08-20.xlsx"
    output_dir = project_root / "NordDRG_AI_Benchmark" / "CSV"
    
    if not input_file.exists():
        print(f"Error: Input file not found at {input_file}")
        sys.exit(1)
        
    output_dir.mkdir(exist_ok=True)
    print(f"Processing file: {input_file}")
    print(f"Output directory: {output_dir}")

    # Read Questions and Answers sheets
    # Header=None because the first few rows are empty/metadata and we want to control the split
    df_q = pd.read_excel(input_file, sheet_name='Questions', header=None)
    df_a = pd.read_excel(input_file, sheet_name='Answers', header=None)

    # Helper to split dataframe based on empty rows
    def split_dataframe(df):
        # Find the row index where the second block starts (Logic vs Grouper)
        # We look for the second occurrence of "Question" or "Right answer" in column 2 (index 2)
        # Or simply look for the empty row separator.
        
        # Based on inspection:
        # Row 2 (index 2) is header for Block 1
        # Row 16 (index 16) is header for Block 2
        # Row 15 is empty
        
        # Block 1: Logic
        # Data starts at index 2 (header) + 1 = 3
        # Ends at index 14
        block1 = df.iloc[2:15].copy()
        # Set first row as header
        block1.columns = block1.iloc[0]
        block1 = block1[1:] # Drop header row
        block1 = block1.dropna(how='all', axis=1) # Drop empty columns (col 0)
        
        # Block 2: Grouper
        # Data starts at index 16 (header)
        block2 = df.iloc[16:].copy()
        block2.columns = block2.iloc[0]
        block2 = block2[1:]
        block2 = block2.dropna(how='all', axis=1)
        
        return block1, block2

    print("Splitting Questions...")
    logic_q, grouper_q = split_dataframe(df_q)
    
    print("Splitting Answers...")
    logic_a, grouper_a = split_dataframe(df_a)

    # Save to CSV
    # We only want the content column.
    # For Questions, it's the column named "Question"
    # For Answers, it's the column named "Right answer"
    
    # Rename columns to be consistent if needed, or just save as is.
    # The user requested specific filenames.
    
    logic_q.to_csv(output_dir / "logic_questions.csv", index=False)
    print(f"Saved logic_questions.csv ({len(logic_q)} rows)")
    
    logic_a.to_csv(output_dir / "logic_answers.csv", index=False)
    print(f"Saved logic_answers.csv ({len(logic_a)} rows)")
    
    grouper_q.to_csv(output_dir / "grouper_questions.csv", index=False)
    print(f"Saved grouper_questions.csv ({len(grouper_q)} rows)")
    
    grouper_a.to_csv(output_dir / "grouper_answers.csv", index=False)
    print(f"Saved grouper_answers.csv ({len(grouper_a)} rows)")

if __name__ == "__main__":
    process_benchmark_qa()
