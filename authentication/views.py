from django.shortcuts import render
from . import forms
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from authentication.models import User
from django.contrib.auth import logout

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
                if user.role == User.ADMIN:
                    return redirect('home')  # Rediriger vers la page d'accueil de l'admin
                elif user.role == User.USER:
                    return redirect('home_user')  # Rediriger vers la page d'accueil de l'utilisateur
                
            message = 'Le nom d\'utilisateur ou le mot de passe que vous avez saisi est incorrect.'
    
    return render(request, 'login.html', {'form': form, 'message': message})


def logout_user(request):
    
    logout(request)
    return redirect('login')

def home(request):    
    return render(request, 'dashboard.html')