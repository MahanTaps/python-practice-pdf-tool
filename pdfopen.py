from magic import magic
import pypdf

def verify_pdf(document):
    return 'PDF'in magic.from_file(document)
    
def first_page_text(document):
    from pypdf import PdfReader
    reader= PdfReader(document)
    page=reader.pages[0]
    print (page.extract_text())

if __name__=="__main__":
    filename="example.pdf" 
    if verify_pdf(filename):
        try:
            first_page_text(filename)
        except Exception as e: 
            print("Exception",e)
    else: 
        print("File is not a PDF!")

