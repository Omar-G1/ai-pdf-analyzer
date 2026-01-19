import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Read PDF and extract text"""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text