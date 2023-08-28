from django.shortcuts import render
from . import forms
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from authentication.models import User
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def change_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            request.user.set_password(password1)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Keep the user logged in
            messages.success(request, 'Password successfully changed.')
            # return redirect('password_change_done')
            
            if(request.user.role  == 'ADMIN'):
                return render(request, 'change_password.html')
            else:
                return render(request, 'change_passwordUser.html')
    
            
        else:
            messages.error(request, 'Passwords do not match.')
            
            if(request.user.role  == 'ADMIN'):
                    return render(request, 'change_password.html')
            else:
                return render(request, 'change_passwordUser.html')
            
    if(request.user.role  == 'ADMIN'):
        return render(request, 'change_password.html')
    else:
        return render(request, 'change_passwordUser.html')

    
    

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