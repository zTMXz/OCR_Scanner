import easyocr
import os
import logging

logger = logging.getLogger('main')

def scan_image(img_path: str, lang: str):
    reader = easyocr.Reader([lang])
    result = reader.readtext(os.path.abspath(os.curdir) + img_path,
                           detail=0, paragraph=True)
    result = ' '.join(i for i in result)

    logger.info('User used text recognition')

    return result

