import easyocr
import os


def scan_image(img_path: str):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(os.path.abspath(os.curdir) + img_path,
                           detail=0, paragraph=True)[0]
    result_extended = reader.readtext(os.path.abspath(os.curdir) + img_path)
    result_extended = '\n'.join([''.join(text + ' -> ' + str(chance)) for borders, text, chance in result_extended])

    return result, result_extended

