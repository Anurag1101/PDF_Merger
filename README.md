# PDF Merger

A Python utility for merging multiple `PDF` files into a single `PDF`. This script, using the `PyPDF2` library, reads a list of specified `PDF` files, merges them, and saves the result as a single `PDF` file. It also includes error handling to ensure smooth operation.

## Features:

- Combines multiple `PDF` files into one.

- Simple to set up and use.
  
- Handles common errors, such as missing files.

- Provides feedback on each file added and the final output.

## Requirements:

- Python 3.x

- PyPDF2 library

You can install the PyPDF2 library with pip:

    pip install PyPDF2

## Setup:

- Clone or download this repository.
  
- Place the `PDF` files you want to merge into the project folder.
  
## Usage:

### Open the script file and modify the pdfiles list with the names of the PDFs you want to merge.

**Example:**

    pdfiles = ["ps.pdf", "py.pdf"]

### Run the script:

    python PDF_Merger.py

### The merged PDF will be saved as `merged.pdf` in the same directory.

## Error Handling:

### The script includes error handling for:

- FileNotFoundError: Checks if the specified PDF files are present. If not, it alerts the user.
  
- General Exceptions: Catches any other unexpected errors that may occur during file processing.

## Output
The merged PDF file is saved as `merged.pdf` in the project folder. Each time the script is run, it will overwrite any existing `merged.pdf` file in the directory.

## Contributions:

`Contributions`, `suggestions`, and `bug reports` are welcome. Feel free to fork the repository and make your changes.

## License:

This project is licensed under the `MIT` License.
