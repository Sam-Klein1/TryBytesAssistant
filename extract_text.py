import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    # Remove new lines and extra spaces
    continuous_text = ' '.join(text.split())

    # Save the continuous text to a file
    with open(output_txt_path, 'w') as text_file:
        text_file.write(continuous_text)

# Example usage
pdf_path = 'marina_pizza.pdf'
output_txt_path = 'extracted.txt'
extract_text_from_pdf(pdf_path, output_txt_path)