from django.contrib.auth import logout
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout 
from .core import get_student_map 

@login_required 
def professor_dashboard(request): 
    if request.user.profile.organisation == "Student": 
        return redirect('/')

    context = {}
    return render(request, 'professor/professor.dashboard.html', context)


@login_required 
def professor_logout(request): 
    logout(request)
    return redirect('/professor')

@login_required
def student_data_view(request): 
    context = {}
    student_map_data = get_student_map()
    for d in student_map_data: 
        print(d.tag_list)
    context['student_map_list'] = student_map_data
    return render(request, 'professor/profesor_student_detail.html', context)