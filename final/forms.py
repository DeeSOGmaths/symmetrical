from django import forms
from captcha.fields import CaptchaField
from PIL import Image
import random



class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'username'}))
    password = forms.CharField(widget = forms.TextInput(attrs={'class':'password'}))
    captcha = CaptchaField(widget = forms.TextInput(attrs={'class':'captcha'}))



class CaptchaForm(forms.Form):
    answer = forms.CharField(widget = forms.TextInput(attrs={'class':'answer'}))

labels = {
            'answer':'Answer'
        }
