import os
import ntpath
import pandas as pd

from src.pdf.parser import extract_information
from settings import OUTPUT_DIR


def create_csv_file(file_path):

    output_file_path = os.path.join(OUTPUT_DIR, ntpath.basename(file_path).replace("pdf", "csv"))
    pdf_info = extract_information(pdf_file_path=file_path)
    categories = list(pdf_info.keys())
    output_info = []
    for category_key in pdf_info.keys():
        output_info.append(pdf_info[category_key])

    pd.DataFrame(output_info).T.to_csv(output_file_path, header=categories, mode="w", index=False)

    print(f"[INFO] Successfully saved in {output_file_path}")

    return output_file_path


if __name__ == '__main__':
    create_csv_file(file_path="")
