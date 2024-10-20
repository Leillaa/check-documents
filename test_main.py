from converters.image_to_text import image_to_text
from converters.pdf_to_text import pdf_to_text
from converters.docx_to_text import docx_to_text
from converters.txt_to_text import txt_to_text
from converters.xlsx_to_text import xlsx_to_text
from converters.odt_to_text import odt_to_text


def test_pdf():
    result = pdf_to_text(r'test_files\test.pdf')
    assert result != None
    print(result)

def test_docx():
    result = docx_to_text(r'test_files\test.docx')
    assert result != None
    print(result)

def test_odt():
    result = odt_to_text(r'test_files\test.odt')
    assert result != None
    print(result)

def test_image():
    result = image_to_text(r'test_files\test.png')
    assert result != None
    print(result)

def test_txt():
    result = txt_to_text(r'test_files\test.txt')
    assert result != None
    print(result)

def test_xlxs():
    result = xlsx_to_text(r'test_files\test.xlsx')
    assert result != None
    print(result)
