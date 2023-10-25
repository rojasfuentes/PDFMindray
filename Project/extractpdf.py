import PyPDF2

from getPDF import pdf_path

def extract_text_from_pdf(pdf_path):
    extracted_text = ""  # Variable para almacenar el texto del PDF
    try:
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            extracted_text += page_text  # Agregar el texto de la página a la variable

        pdf_file.close()

        return extracted_text  # Devolver el texto extraído
    except Exception as e:
        print(f"Ocurrió un error al leer el PDF: {e}")
        return None

pdf_text = extract_text_from_pdf(pdf_path)
#if pdf_text:
#    print(pdf_text) 