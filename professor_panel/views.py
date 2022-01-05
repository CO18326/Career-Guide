from django.contrib.auth import logout
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout 

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