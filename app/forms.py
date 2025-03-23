from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from crispy_forms.layout import Layout,Field,Div

class Login_form(AuthenticationForm):
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"username"}))
    password = forms.CharField(label="password",widget=forms.TextInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"password"}))

class Register_form(UserCreationForm):
    email = forms.EmailField(label="email",widget=forms.EmailInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"email"}))
    first_name =forms.CharField(label="firstname", widget=forms.TextInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"firstname"}))
    last_name = forms.CharField(label="lastname", widget=forms.TextInput(attrs={"class":"bg-white text-black text-xl font-[Rubik] font-semibold","placeholder":"lastname"}))

    class Meta:
        model = User
        fields= ["username","email","first_name","last_name", "password1","password2"]