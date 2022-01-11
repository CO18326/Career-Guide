# utils.py 
# ****************************************
# *********  utility function ************
# ****************************************
import json 
from cs_student_guide_system.settings import MEDIA_ROOT, MEDIA_URL 


def get_json_object(json_filename): 
    try:
        print(MEDIA_ROOT + "/" + str(json_filename))
        course_json_file = open(MEDIA_ROOT + "/" + str(json_filename))
        course_json_object = json.loads(course_json_file.read())
        course_json_file.close()
        return course_json_object 
    except Exception as e: 
        return None 


