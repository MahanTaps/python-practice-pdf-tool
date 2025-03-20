from magic import magic
import pypdf
def verify_pdf(document):
    return 'PDF'in magic.from_file(document)
def first_page_text(document):
    #creating a pdf reader object 
    return None

if __name__=="__main__":
    #takes the example file
    filename="example.pdf" 
    #checks if it is a PDF
    if verify_pdf(filename):
        try:
            with open(filename,'r') as file_example:
                print("File opened!")
        except Exception as e: 
            print("e")
    else: 
        print("File is not a PDF!")

    #Checking the file type