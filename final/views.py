from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from .forms import LoginForm, CaptchaForm
from .models import Captcha, Login
from .utils import generate_key, encrypt_data, decrypt_data
from .forms import EncryptionForm, DecryptionForm


import random, ast


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        captcha_form = CaptchaForm(request.POST)
        if form.is_valid() and captcha_form.is_valid():
            store = Login()
            store.email = form.cleaned_data["email"]
            store.save()
            captcha_answer = request.session['captcha_answer']
            if captcha_form.cleaned_data['answer'].lower() == captcha_answer.lower():
                return redirect('encrypt')  # Redirect to the encryption view after successful login
            else:
                return render(request, 'captcha.html', {'captcha_form': captcha_form, 'error': 'Invalid CAPTCHA', 'captcha_image': request.session['captcha_image'], 'form':form})
            # CAPTCHA validation is handled by the form
            # If the form is valid, the CAPTCHA response was valid
            # Proceed with login logic
        
    else:
        form = LoginForm()
        captcha_form = CaptchaForm()
        captcha = generate_captcha()
        request.session['captcha_image'] = captcha['image']
        request.session['captcha_answer'] = captcha['answer']
        
    return render(request, 'captcha.html', {'form': form, 'captcha_form':captcha_form, 'captcha_image': captcha['image']})



def generate_captcha():
    images = [
        {'image': 'cups.jpg', 'answer': 'cup', 'answer':'Cup'},
        {'image':'bicycles.jpg', 'answer': 'bicycle', 'answer':'Bicycle'},
    ]
    captcha = random.choice(images)
    return captcha



# crypto codes

def encrypt_view(request):
    key = generate_key()
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            key = form.cleaned_data['key']
            encrypted_data = encrypt_data(data, key)
            return render(request, 'encrypted.html', {'encrypted_data': encrypted_data})
    else:
        form = EncryptionForm()
    return render(request, 'encrypt.html', {'key': key, 'form':form})


def decrypt_view(request):
    key =request.session.get('key')
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            encrypted_data = form.cleaned_data['encrypted_data']
            key = form.cleaned_data['key']
            try:
                key = ast.literal_eval(key)
                decrypted_data = decrypt_data(encrypted_data.encode(), key.encode())
                return render(request, 'decrypted.html', {'decrypted_data': decrypted_data})
            except Exception as e:
                return render(request, 'error.html', {'error': str(e)})
    else:
        form = DecryptionForm() #pre-populate the key feild
    return render(request, 'decrypt.html', {'form': form})



