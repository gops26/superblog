from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from crispy_forms.layout import Layout,Field,Div

class Login_form(AuthenticationForm):
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"username"}))
    password = forms.CharField(label="password",widget=forms.TextInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"password"}))
                