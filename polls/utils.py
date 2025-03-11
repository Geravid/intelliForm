# myapp/utils.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(form_data):
    buffer = BytesIO()

    # Create a PDF canvas
    c = canvas.Canvas(buffer, pagesize=letter)

    # Set the title of the document
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Presenter: {form_data['presenter']}")
    c.drawString(100, 730, f"Email: {form_data['email']}")
    c.drawString(100, 710, f"Title: {form_data['title']}")
    c.drawString(100, 690, f"Authors: {form_data['authors']}")
    c.drawString(100, 670, f"Institute: {form_data['institute']}")
    c.drawString(100, 650, f"Resume: {form_data['resume']}")
    c.drawString(100, 630, f"Keywords: {form_data['key_words']}")
    c.drawString(100, 610, f"Modality: {form_data['modality']}")
    c.drawString(100, 590, f"Group: {form_data['group']}")

    # Save the PDF
    c.showPage()
    c.save()

    # Get the PDF content from the buffer
    pdf = buffer.getvalue()
    buffer.close()

    return pdf
