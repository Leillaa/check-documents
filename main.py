from converters.image_to_text import image_to_text
from converters.pdf_to_text import pdf_to_text
from converters.docx_to_text import docx_to_text
from converters.txt_to_text import txt_to_text
from converters.xlsx_to_text import xlsx_to_text
from converters.odt_to_text import odt_to_text
import os

#словарь со всеми функциями конвертерами
converters = {
    '.jpeg': image_to_text,
    '.png': image_to_text,
    '.pdf': pdf_to_text,
    '.docx': docx_to_text,
    '.txt': txt_to_text,
    '.xlsx': xlsx_to_text,
    '.odt': odt_to_text
}

def get_text(file_path) -> None:
    _, file_extension = os.path.splitext(file_path)
    print(converters[file_extension](file_path))

#вызов главной функции с указанием пути к файлу
get_text('test.docx')