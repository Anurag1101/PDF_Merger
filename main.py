import PyPDF2

# List of PDF files to merge
pdfiles = ["ps.pdf", "py.pdf"]

# Created a PdfMerger object
merger = PyPDF2.PdfMerger()

# Merging PDFs with Error Handling
try:
    for filename in pdfiles:
        with open(filename, 'rb') as pdfFile:
            pdfReader = PyPDF2.PdfReader(pdfFile)
            merger.append(pdfReader)
            print(f"Added {filename} to the merger.")
    
    # Named merged output to 'merged.pdf'
    output_filename = 'merged.pdf'
    merger.write(output_filename)
    print(f"Merged PDF saved as '{output_filename}'.")

except FileNotFoundError as e:
    print(f"Error: {e}. Please check that all files in 'pdfiles' exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Closed the merger object i.e. Good Practice
    merger.close()
