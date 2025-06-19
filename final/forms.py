from django import forms
from captcha.fields import CaptchaField
from PIL import Image
import random



class LoginForm(forms.Form):
    email = forms.CharField(label_suffix = '', widget = forms.TextInput(attrs={'class':'email', 'placeholder':'enter your email'}), max_length=100)

    labels = {
        'email':'Email'
    }
    



class CaptchaForm(forms.Form):
    answer = forms.CharField(label_suffix = '', widget = forms.TextInput(attrs={'class':'answer','placeholder':'enter your answer...'}))

labels = {
            'answer':'Answer'
        }

class EncryptionForm(forms.Form):
    data = forms.CharField(label_suffix = '', widget=forms.Textarea(attrs={'class':'data','placeholder':'enter the data you want to encrypt e.g i love Caleb University...'}))
    key = forms.CharField(label_suffix = '', widget=forms.TextInput(attrs={'class':'key','placeholder':'enter your copied key to encrypt...'}))

labels = {
            'data':'Data',
            'key':'Key'
        }
class DecryptionForm(forms.Form):
    encrypted_data = forms.CharField(label_suffix = '', widget=forms.Textarea(attrs={'class':'enc-data','placeholder':'Paste your saved or copied encrypted data here..'}))
    key = forms.CharField(label_suffix = '',widget=forms.TextInput(attrs={'class':'key','placeholder':'Paste your secret key here...'}))

labels = {
            'encrypted_data':'Encrypted_Data',
            'key':'Secret_key'
        }

