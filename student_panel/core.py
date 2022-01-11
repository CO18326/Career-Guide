# filename : core.py 
# ********************************************
# ************** contain function related to work analysis. 
# ******************************************** 
from course_system.models import CourseData, SkillHotWords 
from course_system.views import get_json_object 
from course_system.core import CourseJSONdataExtractor, CourseSkillMap, CourseUnitData 
from typing import List 
from django.contrib.auth.models import User 

class CourseTagMapObject: 

    def __init__(self, course_data : CourseData, tag_txt : str): 
        self.course_data = course_data 
        self.tag_txt = tag_txt 

## function to fetch all course which tag for which are are fethced. 
def get_course_tag_list_student_interest(user : User, skill_name : str) -> List[CourseTagMapObject]:
    course_tag_map_object_list = []
    # fetch course object list. 
    course_list = CourseData.objects().all() 
    list_of_hot_words = SkillHotWords.objects.filter(skill_name = skill_name) # list of all host workds. 

    for course in course_list: 
        course_skill_map = CourseSkillMap(
            course_json_extractor=CourseJSONdataExtractor(get_json_object(course.course_json_file)),
            skill_hot_work_list=list_of_hot_words
        )
        
        if course_skill_map.is_required(): 
            course_tag_map_object_list.append(CourseTagMapObject(course_data=course, tag_txt = skill_name))

    return course_tag_map_object_list # return list of targeted course with tag. 

    

