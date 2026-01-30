from pypdf import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF file and returns the text content.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def load_resumes_from_folder(folder_path):
    """
    Scans a folder for PDFs and returns a dictionary {filename: text}.
    """
    resumes = {}
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found.")
        return resumes

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(path)
            if text:
                resumes[filename] = text
                print(f"Loaded: {filename}")
    return resumes
