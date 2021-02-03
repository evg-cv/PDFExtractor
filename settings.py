import os

from utils.folder_file_manager import make_directory_if_not_exists

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'output'))

TECH_WIDTH_THRESH = 0.2
TECH_HEIGHT_THRESH = 0.9
HEADER_THRESH = 0.96
FOOTER_THRESH = 0.04

PDF_FILE_PATH = ""
