import easyocr
import os


def scan_image(img_path: str, lang: str):
    reader = easyocr.Reader([lang])
    result = reader.readtext(os.path.abspath(os.curdir) + img_path,
                           detail=0, paragraph=True)
    result = ' '.join(i for i in result)

    return result

