from django.shortcuts import redirect, render
from .forms import CourseDataForm 
from .models import CourseData, CourseRegisterBy 
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
            course_register_by.user_id = request.user 
            course_register_by.save()

        context['REG_SUCCESS'] = True 
        context['course_name'] = form.cleaned_data.get('course_name')
        print("------------------")
        
    context['form'] = CourseDataForm 
    return render(request, 'course_system/course_register.html', context)

@login_required 
def show_register_course(request): 
    context = {}
    course_data = CourseRegisterBy.objects.filter(user_id = request.user)
    print(course_data)
    print(MEDIA_ROOT)
    print(MEDIA_URL)
    print(MEDIA_ROOT+MEDIA_URL)
    course_data_list = []
    for course_d in course_data: 
        print(course_d.course_id)
        course_data_list.append(course_d.course_id)

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
        course = CourseData.objects.get(course_id=course_id)
        course_json_object = get_json_object(course.course_json_file)
        context['course_model'] = course 
        context['course_json_object'] = course_json_object 
        course_json_data = CourseJSONdataExtractor(course_json_object)
        context['course_data_object'] = course_json_data 
        
        return render(request, 'course_system/course_data_view.html', context)

    except: 
        return redirect('/coures/viewlist')
