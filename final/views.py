from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from .forms import LoginForm, CaptchaForm
from .models import Captcha
import random


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # CAPTCHA validation is handled by the form
            # If the form is valid, the CAPTCHA response was valid
            # Proceed with login logic
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'ore.html', {'form': form})

# view for home
def home_view(request):
    return render(request, 'home.html')

     #new

def generate_captcha():
    images = [
        {'image': 'cups.jpg', 'answer': 'cup', 'answer':'Cup'},
        {'image':'bicycles.jpg', 'answer': 'bicycle', 'answer':'Bicycle'},
    ]
    captcha = random.choice(images)
    return captcha

def captcha_view(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            captcha_answer = request.session['captcha_answer']
            if form.cleaned_data['answer'].lower() == captcha_answer.lower():
                return render(request, 'captcha.html', {'form': form, 'success':True})
            else:
                return render(request, 'captcha.html', {'form': form, 'error': 'Invalid CAPTCHA',})
    else:
        captcha = generate_captcha()
        request.session['captcha_image'] = captcha['image']
        request.session['captcha_answer'] = captcha['answer']
        form = CaptchaForm()
    return render(request, 'captcha.html', {'form': form, 'captcha_image': captcha['image']})

