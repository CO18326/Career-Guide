from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout
from user.models import profile 

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

@login_required 
def professor_list(request): 
    context = {}
    try: 
        professor_list = profile.objects.filter(organisation = 'Profesor')
        context['profesor_list'] = professor_list 
        return render(request, 'student_panel_professor_list.html', context)
    except: 
        context['professor_list'] = []
        return render(request, 'student_panel_professor_list.html')
