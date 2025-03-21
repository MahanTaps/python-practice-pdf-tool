from pdfopen import verify_pdf

def test_verify_pdf():
    assert verify_pdf("test.pdf")==True, "This is a PDF so it should be true"
    assert verify_pdf("example.pdf")==False, "This is a PDF so it should be true"
    assert verify_pdf("README.txt")==True, "This is not a pdf, so it should be false"
