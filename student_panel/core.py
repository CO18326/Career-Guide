# filename : core.py 
# ********************************************************************
# ************** contain function related to work analysis. **********
# ******************************************************************** 
from course_system.models import CourseData, CourseEnroll, SkillHotWords,studentDomain  
from course_system.views import get_json_object 
from course_system.core import CourseJSONdataExtractor, CourseSkillMap, CourseUnitData 
from typing import List 
from django.contrib.auth.models import User 
from .utils import StudentCourseMap 
from course_system.core import get_tag_course



# * function for generate course -> StudentCourseMap <- list 
# * according for prefrence and fire the list. 
def list_course_student_preferece(user : User) -> List[StudentCourseMap]:
    student_map_course_list = []
    # list of enrolled coursed by student. 
    enrolled_coursed_list = CourseEnroll.objects.filter(student_id  = user)
    enroll_course_l = [el.course_id for el in enrolled_coursed_list]
    course_interest_list = []
    intersted_skill = studentDomain.objects.filter(user_id = user)
    skill_list = [sk.skill_name for sk in intersted_skill]
    # list of all coursed. 
    list_of_course = CourseData.objects.all()
    for course in list_of_course:
        print("...")
        print(get_tag_course(course)) 
        print("....")
        if if_element_in(get_tag_course(course), skill_list): 
            course_interest_list.append(course)
   
    for course in course_interest_list: 
        if course in enroll_course_l: 
            student_map_course_list.append(
                StudentCourseMap(
                    course_data = course, 
                    tag_list = get_tag_course(course), 
                    enroll = True 
                )
            )
        else: 
            student_map_course_list.append(
                StudentCourseMap(
                    course_data = course, 
                    tag_list = get_tag_course(course), 
                    enroll = False 
                )
            )
    # *student map course list. 
    return student_map_course_list 

    
def if_element_in(lst_1, lst_2): 
    for ele in lst_1: 
        if ele in lst_2: 
            return True 
    return False 