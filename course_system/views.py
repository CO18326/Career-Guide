from django.shortcuts import redirect, render
from .forms import CourseDataForm 
from .models import CourseData 
from cs_student_guide_system.settings import MEDIA_ROOT, MEDIA_URL
from .course_utils import CourseJSONParse 
import json 


def register_course(request): 
    if request.method == "POST": 
        form = CourseDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {}
    context['form'] = CourseDataForm 
    return render(request, 'course_system/course_register.html', context)


def show_register_course(request): 
    context = {}
    course_data = CourseData.objects.all()
    print(MEDIA_ROOT)
    print(MEDIA_URL)
    print(MEDIA_ROOT+MEDIA_URL)

    for course in course_data: 
        course_json_data_file = open(MEDIA_ROOT + "/" +str(course.course_json_file))
        try:
            course_json_object = json.loads(course_json_data_file.read())
            print(course_json_object)

        except Exception as e: 
            print("File is not Json")
        course_json_data_file.close()

    context['course_data'] = course_data 
    return render(request, 'course_system/course_list_view.html', context)


def view_coures_coures_id(request, courese_id): 
    context = {}
    try: 
        course = CourseData.objects.get(courese_id=courese_id)
        course_json_data_file = open(MEDIA_ROOT + "/" +str(course.course_json_file))
        course_json_object = json.loads(course_json_data_file.read())
        course_json_data_file.close()
        
        
    except: 
        redirect('/coures/viewlist')
