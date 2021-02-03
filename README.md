# PDFExtractor

## Overview

This project is to extract the necessary information from the pdf file and save them into the csv file. The PDFMiner and 
Pandas libraries are used in this project.

## Structure

- output

    The directory to save the result csv files
    
- src

    The main source code to extract the necessary information and save into the csv file.

- utils

    The source code for management of files and folders of the project
    
- app

    The main execution file
    
- requirements

    All the dependencies for this project
    
- settings

    Several settings including the pdf file path
    
## Installation

- Environment

    Ubuntu 18.04, Windows 10, Python 3.6
    
- Dependency Installation

    Please navigate to this project directory and run the following command in the terminal.
    
    ```
        pip3 install -r requirements.txt
    ```

## Execution

- Please set PDF_FILE_PATH variable in settings file with the full path of pdf file to process.

- Please run the following command in the terminal.

    ```
        python3 app.py
    ```
