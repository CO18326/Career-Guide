from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.contrib.auth import logout

@login_required 
def student_panel_home_page(request): 
    if request.user.profile.organisation == "Profesor": 
        return redirect('/professor')
    student_panel_home_data = {}
    return render(request, 'student_panel/student_panel_home.html', student_panel_home_data)


@login_required 
def logout_user(request):
    logout(request)
    return redirect('/')