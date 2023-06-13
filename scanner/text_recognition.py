import easyocr
import os

def scan_image(img_path: str):
    reader = easyocr.Reader(['en'])
    print('---', os.path.abspath(os.curdir))
    return reader.readtext(os.path.abspath(os.curdir) + '\\' + img_path,
                             detail=0, paragraph=True)[0]