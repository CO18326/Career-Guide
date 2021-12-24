from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

@login_required 
def student_panel_home_page(request): 
    student_panel_home_data = {}
    return render(request, 'student_panel/student_panel_home.html', student_panel_home_data)
