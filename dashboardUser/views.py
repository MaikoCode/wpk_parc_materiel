from django.shortcuts import render

from django.contrib.auth.decorators import login_required, user_passes_test

def is_user(user):
    return user.role == 'USER'

@login_required
@user_passes_test(is_user)

def dashboardUserView(request):
    

    return render(request, 'dashboardUser.html')
