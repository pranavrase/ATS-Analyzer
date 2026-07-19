import PyPDF2
from docx import Document


def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def read_docx(file):
    doc = Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text