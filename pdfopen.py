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
    #takes the example file
    filename="example.pdf" 
    #checks if it is a PDF
    if verify_pdf(filename):
        try:
            with open(filename,'r') as file_example:
                print("File opened!")
            first_page_text(filename)
        except Exception as e: 
            print("e")
    else: 
        print("File is not a PDF!")

    #Checking the file type