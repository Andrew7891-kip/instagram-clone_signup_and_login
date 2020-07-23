from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.CharField(max_length=250,
                required=True,
                label='Email', 
                widget=forms.EmailInput(
                    attrs= {'placeholder':"Enter Mobile number or Email"} )
                )
    full_name=forms.CharField(label='Full Name',
                max_length=250,
                required=True,
                widget=forms.TextInput(attrs= {
                    'placeholder':"Enter Full Name"})
                )
    username=forms.CharField(label='Username',
                max_length=250,
                required=True,
                widget=forms.TextInput(attrs= {
                    'placeholder':"Enter Username"})
                )
    password1=forms.CharField( label='Password' ,
                max_length=250,
                required=True,
                widget=forms.PasswordInput(attrs= {
                    'placeholder':"Enter Password"})
                )
    password2=forms.CharField(label='Confirm Password',
                max_length=250,
                required=True,
                widget=forms.PasswordInput(attrs= {
                    'placeholder':"Confirm password"})
                )
    class Meta:
        model=User
        fields=('email','full_name','username','password1','password2')