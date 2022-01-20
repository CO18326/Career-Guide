from django.shortcuts import redirect, render
from .forms import CourseDataForm 
from .models import CourseData, CourseRegisterBy, CourseEnroll  
from cs_student_guide_system.settings import MEDIA_ROOT, MEDIA_URL
from .course_utils import CourseJSONParse 
from django.contrib.auth.decorators import login_required 
import json 
from .utils import get_json_object 
from .core import CourseJSONdataExtractor 

@login_required 
def register_course(request): 
    context = {}
    context['REG_SUCCESS'] = False 
    if request.method == "POST": 
        form = CourseDataForm(request.POST, request.FILES)
        if form.is_valid():
            course_object = form.save()
            course_register_by = CourseRegisterBy()
            course_register_by.course_id = course_object
            course_register_by.user_id = request.user.profile  
            course_register_by.save()

        context['REG_SUCCESS'] = True 
        context['course_name'] = form.cleaned_data.get('course_name')
        print("------------------")
        
    context['form'] = CourseDataForm 
    return render(request, 'course_system/course_register.html', context)

@login_required 
def show_register_course(request): 
    context = {}
    if request.user.profile.organisation == "Profesor":
        course_data = CourseRegisterBy.objects.filter(user_id = request.user)
        print(course_data)
        print(MEDIA_ROOT)
        print(MEDIA_URL)
        print(MEDIA_ROOT+MEDIA_URL)
        course_data_list = []
        for course_d in course_data: 
            print(course_d.course_id)
            course_data_list.append(course_d.course_id)
    else: 
        course_data_list = CourseData.objects.all() # get all course for students. 
    print(course_data_list)

    for course in course_data_list: 
        try:
            # print(course_json_object)
            json_object = get_json_object(course.course_json_file)
            print("-------------------")
            print(json_object)
            print("--------------------")

        except Exception as e: 
            print("File is not Json")

    context['course_data'] = course_data_list
    return render(request, 'course_system/course_list_view.html', context)

@login_required 
def view_coures_coures_id(request, course_id): 
    context = {}
    try: 
        if request.user.profile.organisation == 'Student': 
            pass 
        course = CourseData.objects.get(course_id=course_id)
        course_json_object = get_json_object(course.course_json_file)
        context['course_model'] = course 
        context['course_json_object'] = course_json_object 
        course_json_data = CourseJSONdataExtractor(course_json_object)
        context['course_data_object'] = course_json_data 

        # * if viewer is student.
        if request.user.profile.organisation == "Student": 
            print("****** student **********")
            context['student_view'] = True 
            enrolled_course = CourseEnroll.objects.filter(student_id = request.user)
            enrolled_courses_list = []
            for course_d in enrolled_course: 
                enrolled_courses_list.append(course_d.course_id)
            if course in enrolled_courses_list: 
                context['student_enrolled'] = True 
            print(course)
            print(enrolled_courses_list)
        else:
            context['student_view'] = False 
            context['student_enrolled'] = False 


        return render(request, 'course_system/course_data_view.html', context)

    except: 
        return redirect('/coures/viewlist')

@login_required 
def student_course_enroll(request, course_id): 
    if request.user.profile.organisation == "Student": 
        print("-----------------")
        course_data = CourseData.objects.get(course_id = course_id)
        enroll_obj = CourseEnroll()
        enroll_obj.course_id = course_data 
        enroll_obj.student_id = request.user 
        enroll_obj.save() # enroll student. 
        return redirect(f'/course/courseview/{course_id}')
    return redirect(f'/course/courseview/{course_id}')