import logging 
from course_system.models import studentDomain 
from user.models import profile 
from django.contrib.auth.models import User 
from course_system.core import get_student_tag_list 
from typing import List 
from .utils import StudentTagMap 

# *get logger. 
logger = logging.getLogger(__name__)


def get_student_map(): 
    student_tag_map_list = []
    # * get list of students. 
    student_profile_data = profile.objects.filter(organisation = 'Student')
    for student in student_profile_data: 
        student_tag_list = get_student_tag_list(student_profile_object=student)
        student_tag_list_init = studentDomain.objects.filter(user_id = User.objects.get(username = student.user.username))
        student_tag_map_list.append(
            StudentTagMap(
                student_profile_data=student, 
                tag_list_course=list(set(student_tag_list)), 
                tag_list_interest=list(set([st.skill_name for st in student_tag_list_init]))
            )
        )
    return student_tag_map_list 