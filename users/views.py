from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator

from OCR_Scanner.settings import EMAIL_HOST_USER
from users.forms import UserCreationForm, UserUpdateForm
from scanner.models import Scanner


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            print(form)
            login(request, user)

            send_mail(subject='Successful Registration Message',
message= f"""
You have successfully registered on DockieScanner
Your login details:
===============================
    username: {username}
    password: {password}
===============================
""",
                      recipient_list=[email],
                      from_email=EMAIL_HOST_USER
                      )

            return redirect('home')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)


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
