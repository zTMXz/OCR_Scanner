from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView

from .forms import ScannerForm
from .models import Scanner
from scanner.text_recognition import scan_image


class ImageUpload(CreateView):
    template_name = 'scanner/scan.html'
    form_class = ScannerForm

    def form_valid(self, form):
        img_obj = form.instance.image

        form.instance.user = self.request.user
        form.save()

        form.instance.recognition, form.instance.recognition_extended = scan_image(img_obj.url)
        form.save()

        return super().form_valid(form)


class ImageUploadDetail(DetailView):
    template_name = 'scanner/scan_success.html'
    model = Scanner
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Scanner, id=id_)
