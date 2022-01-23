# utils.py 
# *****************************************************
# ******************* Course Data Mapping ************* 
from course_system.views import get_json_object 
from course_system.models import CourseData, CourseRegisterBy, DomainData
from course_system.core import CourseSkillMap 
from user.models import profile 

## model contain data regarding Student and Courses.
## this model will be specific for a student. 
class StudentCourseMap: 
    def __init__(self,course_data : CourseData, tag_list : list, enroll : bool): 
        self.course_data = course_data 
        self.tag_list = tag_list 
        self.enroll = enroll
