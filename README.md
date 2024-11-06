# PDF Merger

A Python utility for merging multiple PDF files into a single PDF. This script, using the `PyPDF2` library, reads a list of specified PDF files, merges them, and saves the result as a single PDF file. It also includes error handling to ensure smooth operation.

## Features:

- Combines multiple PDF files into one.

- Simple to set up and use.
  
- Handles common errors, such as missing files.

- Provides feedback on each file added and the final output.

Requirements
Python 3.x
PyPDF2 library
You can install the PyPDF2 library with pip:

bash
Copy code
pip install PyPDF2
Setup
Clone or download this repository.
Place the PDF files you want to merge into the project folder.
Usage
Open the script file and modify the pdfiles list with the names of the PDFs you want to merge.
Example:
python
Copy code
pdfiles = ["ps.pdf", "py.pdf"]
Run the script:
bash
Copy code
python PDF_Merger.py
The merged PDF will be saved as merged.pdf in the same directory.
Example Code
python
Copy code
import PyPDF2

# List of PDF files to merge
pdfiles = ["ps.pdf", "py.pdf"]

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Try merging PDFs with error handling
try:
    for filename in pdfiles:
        with open(filename, 'rb') as pdfFile:
            pdfReader = PyPDF2.PdfReader(pdfFile)
            merger.append(pdfReader)
            print(f"Added {filename} to the merger.")
    
    # Write the merged output to 'merged.pdf'
    output_filename = 'merged.pdf'
    merger.write(output_filename)
    print(f"Merged PDF saved as '{output_filename}'.")

except FileNotFoundError as e:
    print(f"Error: {e}. Please check that all files in 'pdfiles' exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Clean up the merger object
    merger.close()
Error Handling
The script includes error handling for:

FileNotFoundError: Checks if the specified PDF files are present. If not, it alerts the user.
General Exceptions: Catches any other unexpected errors that may occur during file processing.
Output
The merged PDF file is saved as merged.pdf in the project folder. Each time the script is run, it will overwrite any existing merged.pdf file in the directory.

Contributions
Contributions, suggestions, and bug reports are welcome. Feel free to fork the repository and make your changes.

License
This project is licensed under the MIT License.
