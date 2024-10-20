

def txt_to_text(file_path) -> list:
    with open(file_path, encoding='utf-8') as file:
        text = [line.strip() for line in file.readlines() if line.strip()]

        return text