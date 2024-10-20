import docx


def docx_to_text(file_path) -> list:
    doc = docx.Document(file_path)
    text = [row.text for row in doc.paragraphs if row.text]

    return text
