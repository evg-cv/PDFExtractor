from src.csv.converter import create_csv_file
from settings import PDF_FILE_PATH


if __name__ == '__main__':
    create_csv_file(file_path=PDF_FILE_PATH)
