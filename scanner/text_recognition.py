import easyocr

def scan_image(img_path: str):
    reader = easyocr.Reader(['en'])
    return reader.readtext('C:/Users/erekh/PycharmProjects/OCR_Scanner' + img_path,
                             detail=0, paragraph=True)[0]