from django.contrib.auth.backends import RemoteUserBackend
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout
from user.models import profile 
from course_system.models import DomainData, DomainName, studentDomain, CourseEnroll  
from user.models import profile 
from .utils import ProfesorData 

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

    professor_list = profile.objects.filter(organisation = 'Profesor')
    print(professor_list)
    for profesor in professor_list: 
        profesor_data = ProfesorData(profile_data=profesor)
        professor_data_list = profesor_data.get_domain()
        print(professor_data_list)
    context['profesor_list'] = professor_list         
    return render(request, 'stuent_panel/student_panel_professor_list.html', context)

@login_required 
def update_domain(request): 
    context = {}
    context['domain_list'] = DomainData.objects.all() # get list of all domain name. 
    print(DomainData.objects.all())
    if request.method == "POST": 
        ## update user prefrence. 
        domain_name = request.POST.get('domainname')
        print(domain_name)
        domain_data = studentDomain()
        domain_data.user_id = request.user 
        domain_data.skill_name = domain_name
        domain_data.save() # save domain data. 
        context['domain_added'] = True     
        context['domain_name'] = domain_name
        domain_name = request.POST.get('domainname')
        print("############################")
        print(domain_name)
        return render(request, 'student_panel/student_domain_update.html', context)
    else: 
        return render(request, 'student_panel/student_domain_update.html', context)



@login_required 
def get_enrolled_course_list(request): 
    context = {}
    context['NO_ENROLL'] = False 
    list_of_courses = [data.course_id for data in CourseEnroll.objects.filter(student_id = request.user)]
    print(list_of_courses)
    if list_of_courses == []: 
        context['NO_ENROLL'] = True 
    context['course_list'] = list_of_courses 
    for course in context['course_list']: 
        print(course.course_name)
    return render(request, 'student_panel/student_course_enroll.html', context)

