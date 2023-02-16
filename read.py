# extract_doc_info.py
import PyPDF2
from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information
def read_content(path):
    # creating a pdf reader object
    reader = PyPDF2.PdfReader(path)

    # print the number of pages in pdf file
    print(len(reader.pages))
    # print the text of the first page
    pg = int(input("Enter Page Nummber"))
    print(reader.pages[pg-1].extract_text())

if __name__ == '__main__':
    path = r'C:\Users\thejr\OneDrive\Desktop\new\sample.pdf'
    extract_information(path)
    # read_content(path)