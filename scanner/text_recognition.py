import easyocr
import os


def scan_image(img_path: str):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(os.path.abspath(os.curdir) + '\\' + img_path,
                           detail=0, paragraph=True)[0]
    result_extended = reader.readtext(os.path.abspath(os.curdir) + '\\' + img_path)

    print(result_extended)
    result_extended = '\n'.join([''.join(t + ' -> ' + str(s)) for b, t, s in result_extended])

    print(result_extended)
    return result, result_extended

