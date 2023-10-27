# import the python module
import PyPDF2

pdf_file = open("sample.pdf", "rb")
PDF_Reader = PyPDF2.PdfReader(pdf_file)
text = PDF_Reader.pages[0].extract_text()
print(text)
