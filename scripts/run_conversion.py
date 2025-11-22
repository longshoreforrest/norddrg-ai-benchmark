import sys
from pathlib import Path

# Add project root to sys.path to allow importing utils
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from utils.xlsx_converter import ExcelToCsvConverter

def main():
    files_to_process = [
        {
            "dir": "NordDRG_FIN2026PL0",
            "filename": "2024-04-15_FIN2026PL0_xlsx_wo_drgs.xlsx"
        },
        {
            "dir": "NordDRG_Combined2024PL",
            "filename": "2023-06-14_Combined2024PL_xls.xlsx"
        }
    ]

    converter = ExcelToCsvConverter()

    for file_info in files_to_process:
        target_dir = project_root / file_info["dir"]
        input_file_path = target_dir / file_info["filename"]

        print(f"\nStarting conversion for file: {input_file_path}")

        try:
            converter.process_file(input_file_path)
            print(f"Done with {file_info['filename']}!")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error processing {file_info['filename']}: {e}")

if __name__ == "__main__":
    main()
