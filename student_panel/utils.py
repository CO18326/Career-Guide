# utils.py 
# *****************************************************
# ******************* Course Data Mapping ************* 
from course_system.views import get_json_object 
from course_system.models import CourseData, CourseRegisterBy, DomainData
from course_system.core import CourseSkillMap 
from user.models import profile 
from .core import  get_professor_tag_list


# ************ Pofessor data class *******************
class ProfesorData: 

    def __init__(self, profile_data : profile):
        self.__profile_data = profile_data  
    
    def get_first_name(self) -> str: 
        return self.__profile_data.firstname 
    
    def get_second_name(self) -> str: 
        return self.__profile_data.lastname 

    def get_branch(self) -> str: 
        return self.__profile_data.branch 
    
    # *Analyse the course registered by the Profesor 
    # *than tag professor according to analysis. 
    def get_domain(self) -> list:
        # get user correspont to profile.  
        user_object = profile.user
        course_list = CourseRegisterBy.objects.filter(user_id = user_object)
        skill_list = DomainData.objects.all() 
        main_list = []
        for skill in skill_list: 
            tag_list = get_professor_tag_list(course_list=course_list, skill_name=skill)
            main_list.extend(tag_list)
        
        return list(set(main_list))