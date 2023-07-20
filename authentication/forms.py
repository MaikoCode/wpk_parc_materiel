
from django import forms

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=63, label='Username')
#     password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=63, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
