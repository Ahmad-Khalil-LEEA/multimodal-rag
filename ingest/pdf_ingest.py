import os
from pdf2image import convert_from_path
import PyPDF2

def process_pdf(pdf_path):
    pdf_id = os.path.splitext(os.path.basename(pdf_path))[0]
    out_dir = f"data/samples/{pdf_id}/slides"
    os.makedirs(out_dir, exist_ok=True)

    # Extract images
    images = convert_from_path(pdf_path)
    for i, img in enumerate(images):
        img.save(f"{out_dir}/slide{i:03d}.jpg", "JPEG")

    # Extract text
    reader = PyPDF2.PdfReader(pdf_path)
    slide_texts = []
    for page in reader.pages:
        slide_texts.append(page.extract_text())
    # Save images and texts to database
    return pdf_id
