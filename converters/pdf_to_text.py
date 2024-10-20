from pdf2image import convert_from_path
import os
from PIL import Image
from converters.image_to_text import image_to_text
from constants import POPPLER_PATH



def pdf_to_text(file_path) -> list:
    images = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    text = []

    for image in images:
        image.save('image.jpeg', 'JPEG')
        result = image_to_text('image.jpeg')
        text.extend(result)
        os.remove('image.jpeg')

    return text
