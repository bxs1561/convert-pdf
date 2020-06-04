from fpdf import FPDF
import PyPDF2

def conver_file_to_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    # pdf.cell(200, 10, txt="university", ln=1, align='C')
    # pdf.cell(200, 10, txt="good morning.", ln=2, align='C')
    with open("diff-two-arrays.txt", "r") as file:
        for f in file:
            pdf.cell(200, 10, txt=f, ln=1, align='C')

    pdf.output("textpdf.pdf")

def get_text_from_pdf():
    file = open("textpdf.pdf",'rb')
    pdf_read = PyPDF2.PdfFileReader(file)
    print(pdf_read.numPages)

    page = pdf_read.getPage(0)
    print(page.extractText())

    file.close()

def main():
    get_text_from_pdf()
    # conver_file_to_pdf()


if __name__ == '__main__':
    main()
