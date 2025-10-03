import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF floor plan.
    Returns a list of strings (per page)
    """
    texts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
    return texts
