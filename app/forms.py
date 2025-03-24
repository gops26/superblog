from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.models import User
from crispy_forms.layout import Layout,Field,Div,Column,Row
from .models import Blog

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

class BlogUploadForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content", "cover_image"]

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field("title",css_class="bg-red-100 text-red-900 text-xl font-[Rubik] font-semibold", label_class="text-red-500 text-xl font-[Rubik] font-semibold"),
                Field("content",css_class="bg-red-100 text-red-900 text-xl font-[Rubik] font-semibold", label_class="text-red-500 text-xl font-[Rubik] font-semibold"),
                Field("coverimage",css_class="bg-red-100 text-red-900 text-xl font-[Rubik] font-semibold", label_class="text-red-500 text-xl font-[Rubik] font-semibold")

            )
        )