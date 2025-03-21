from pdfopen import verify_pdf
from pdfopen import first_page_text
from io import StringIO
import sys
def test_verify_pdf():
    assert verify_pdf("test.pdf")==True, "This is a PDF so it should be true"
    assert verify_pdf("example.pdf")==False, "This is a PDF so it should be true"
    assert verify_pdf("README.txt")==True, "This is not a pdf, so it should be false"
def test_first_page_text():
    sys.stdout=StringIO()
    first_page_text("example.pdf")
    output=sys.stdout.getvalue().strip()
    sys.stdout=sys.__stdout__

    assert (len(output)>0)==True, "Text should be scraped from the PDF, so it should be true"
