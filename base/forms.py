from django import forms
from .models import CustomUser
from django_recaptcha.fields import ReCaptchaField
from allauth.account.forms import (
    SignupForm,
)

class UserEditForm(forms.ModelForm): # 以下追記箇所
  picture = forms.FileField(label='picture', required=False)
  username = forms.CharField(label='user name')
  email = forms.EmailField(label='email')
  description = forms.CharField(label='自己紹介', widget=forms.Textarea) 

  class Meta:
    model = CustomUser
    fields = ('picture', 'username', 'email', 'description')

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    captcha = ReCaptchaField(widget=widgets.ReCaptchaV3)