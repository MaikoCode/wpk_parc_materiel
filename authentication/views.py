from django.shortcuts import render
from . import forms
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Le nom d\'utilisateur ou le mot de passe que vous avez saisie est incorrecte'
    return render(request, 'login.html', {'form': form, 'message': message})


def logout_user(request):
    
    logout(request)
    return redirect('login')

def home(request):    
    return render(request, 'dashboard.html')