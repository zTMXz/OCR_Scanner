from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator

from users.forms import UserCreationForm, UserUpdateForm
from scanner.models import Scanner
from users.send_message import send_message

import os


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        context = {
            'form': form
        }

        return_page = render(request, self.template_name, context)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)

            if os.environ.get('EMAIL_HOST_USER', default=None):
                email_host_user = os.environ.get('EMAIL_HOST_USER')
                send_message(username, password, email, email_host_user)

            return_page = redirect('home')

        return return_page


class Profile(View):
    template_name = 'registration/profile.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")

        scan_history = Scanner.objects.filter(user=request.user).order_by('-id')
        paginator = Paginator(scan_history, 5)
        page_number = request.GET.get('page')
        scan_history = paginator.get_page(page_number)

        context = {
            "form": UserUpdateForm(),
            "scan_history": scan_history
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("login")

        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')


def delete_one(request, scan_id):
    item = Scanner.objects.get(id=scan_id)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_all(request):
    Scanner.objects.filter(user=request.user).delete()
    return redirect('profile')
