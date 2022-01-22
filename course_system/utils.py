# utils.py 
# ****************************************
# *********  utility function ************
# ****************************************
import json 
from cs_student_guide_system.settings import MEDIA_ROOT, MEDIA_URL 
from .models import CourseData 


def get_json_object(json_filename): 
    try:
        print(MEDIA_ROOT + "/" + str(json_filename))
        course_json_file = open(MEDIA_ROOT + "/" + str(json_filename))
        course_json_object = json.loads(course_json_file.read())
        course_json_file.close()
        return course_json_object 
    except Exception as e: 
        return None 


def get_json_object_course(course : CourseData): 
    ## get course file using json object. 
    return get_json_object(course.course_json_file)