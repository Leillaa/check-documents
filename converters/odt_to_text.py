import ezodf


def odt_to_text(file_path) -> list:
    odt = ezodf.opendoc(file_path)
    text = []

    for i in odt.body:
        if i.text != None:
            text.append(i.text)

    return text
