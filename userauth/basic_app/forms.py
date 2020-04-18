from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProInfoForm(forms.ModelForm):
    class Meta():
        model = UserProInfo
        fields=('profile_pics','portfolio_site')
