from django.shortcuts import render
from .forms import ScannerForm
from .models import ScanHistory

import easyocr

try:
    from PIL import Image
except:
    import Image


# Create your views here.
def image_upload(request):
    reader = easyocr.Reader(['en'])

    if request.method == 'POST':
        form = ScannerForm(request.POST, request.FILES)
        if form.is_valid():
            scan_request = form.save(commit=False)
            scan_request.user = request.user
            scan_request.save()

            img_obj = form.instance
            print(img_obj.image.url)
            result = reader.readtext('C:/Users/erekh/PycharmProjects/OCR_Scanner' + img_obj.image.url,
                                     detail=0, paragraph=True)[0]

            ScanHistory.objects.create(user=request.user, description=scan_request.description, image=img_obj.image.url,
                                       recognition=result)

            return render(request, 'scanner/scan.html', {'form': form, 'img_obj': img_obj, 'result': result})
    else:
        form = ScannerForm()
    return render(request, 'scanner/scan.html', {'form': form})
