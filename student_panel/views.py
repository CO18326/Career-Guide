from django.contrib.auth.backends import RemoteUserBackend
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout
from user.models import profile 
from course_system.models import CourseRegisterBy, DomainData, DomainName, studentDomain, CourseEnroll  
from user.models import profile 
from course_system.utils import CourseTagList, ProfesorTagList 
from course_system.core import get_tag_course,get_professor_tag_list
from .core import list_course_student_preferece

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
    profesor_list = profile.objects.filter(organisation='Profesor')
    profesor_obj_tag_map_list = [ProfesorTagList(profile_data=prof,tag_list=get_professor_tag_list(prof)) for prof in profesor_list]
    context['profesor_tag_list'] = profesor_obj_tag_map_list
    return render(request, 'student_panel/student_panel_professor_list.html', context)

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
    
    ## get list of course in tag. 
    list_course_tag = [CourseTagList(course_data = course,tag_list=get_tag_course(course)) for course in list_of_courses]

    print(list_of_courses)
    if list_of_courses == []: 
        context['NO_ENROLL'] = True 
    context['course_list'] = list_of_courses
    context['list_course_tag'] = list_course_tag  
    for course in context['course_list']: 
        print(course.course_name)
    return render(request, 'student_panel/student_course_enroll.html', context)

@login_required 
def get_profesor_course(request,username): 
    context = {}
    user = User.objects.get(username=username)
    professor_profile = profile.objects.get(user = user)
    ## get all courses by targe professor. 
    
    course_list = CourseRegisterBy.objects.filter(user_id = professor_profile)



    if course_list == []: 
        context['valid'] = False 
    else:
        course_list_prof = [data.course_id for data in course_list]
        print(course_list_prof)
        list_course_tag = [CourseTagList(course_data = course, tag_list=get_tag_course(course)) for course in course_list_prof]  
        context['valid'] = True 
        context['list_course_tag'] = list_course_tag 
    return render(request, 'student_panel/student_panel_prof_course.html',context)


@login_required 
def student_intrest_course_list(request): 
    context = {}
    course_map_list = list_course_student_preferece(request.user)
    print("-------------------------")
    print(course_map_list)
    print("---------------------------")
    context['course_map_list'] = course_map_list 
    return render(request, 'student_panel/student_panel_interest_course.html',context)