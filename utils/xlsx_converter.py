import os
import pandas as pd
from pathlib import Path

class ExcelToCsvConverter:
    """
    A utility class to process Excel files and export each sheet as a CSV file.
    """
    
    def __init__(self):
        pass

    def process_file(self, input_file_path: str, output_dir_name: str = "CSV"):
        """
        Reads an Excel file and exports all sheets as CSV files into a subdirectory.

        Args:
            input_file_path (str): Path to the source Excel file.
            output_dir_name (str): Name of the subdirectory to create for CSVs. Defaults to "CSV".
        """
        input_path = Path(input_file_path)
        
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_file_path}")

        # Define output directory path relative to the input file's parent directory
        output_dir = input_path.parent / output_dir_name
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        print(f"Output directory ensured at: {output_dir}")

        try:
            print(f"Reading Excel file: {input_path}...")
            # Read all sheets
            xls = pd.ExcelFile(input_path)
            
            for sheet_name in xls.sheet_names:
                print(f"Processing sheet: {sheet_name}")
                df = pd.read_excel(xls, sheet_name=sheet_name)
                
                # Construct output filename
                # Sanitize sheet name to be safe for filenames if necessary, 
                # but usually simple sheet names are fine.
                safe_sheet_name = "".join([c for c in sheet_name if c.isalnum() or c in (' ', '_', '-')]).strip()
                output_file = output_dir / f"{safe_sheet_name}.csv"
                
                df.to_csv(output_file, index=False)
                print(f"Saved: {output_file}")
                
            print("Conversion completed successfully.")
            
        except Exception as e:
            print(f"An error occurred during processing: {e}")
            raise
