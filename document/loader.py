from pdf2image import convert_from_path
import pdfplumber

def load_pdf(path):
    images = convert_from_path(path, dpi=300)
    text_pages = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text_pages.append(page.extract_text())

    return images, text_pages
