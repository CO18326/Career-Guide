# filname : core.py
# *******************************************************
# **************** Course Json data extractor *********** 
# *******************************************************

from course_system.models import CourseData, CourseRegisterBy, DomainData, SkillHotWords, CourseEnroll  
from .constants import (
    COURSE_SUBJECT_NAME, 
    COURSE_PRE_REQUEST, 
    COURSE_APPLICATIONS, 
    COURSE_OUTCOMES, 
    COURSE_PATH, 
    COURSE_UNIT_NAME, 
    COURSE_UNIT_DES, 
    COURSE_UNIT_LINK, 
    COURSE_UNIT_OUTCOMES, 
)
from .utils import get_json_object_course
from user.models import profile 
from django.contrib.auth.models import User 

class CourseJSONdataExtractor: 

    def __init__(self, course_json_object : dict):
        self.__course_json_object = course_json_object 
        # initlize required data 
        self.__subject_name = self.__course_json_object.get(COURSE_SUBJECT_NAME)
        self.__course_path = self.__course_json_object.get(COURSE_PATH)
        self.__course_pre_request = self.__course_json_object.get(COURSE_PRE_REQUEST)
        self.__course_outcomes = self.__course_json_object.get(COURSE_OUTCOMES)
        print(self.__course_outcomes)
        self.__course_application = self.__course_json_object.get(COURSE_APPLICATIONS)
    
    def get_subject_name(self) -> str: 
        return self.__subject_name 

    def get_course_path(self) -> list: 

        course_path_keys = list(self.__course_path.keys())
        course_unit_list = []
        for unit in course_path_keys: 
            course_unit_list.append(CourseUnitData(self.__course_path.get(unit)))

        return course_unit_list  

    def get_course_pre_request(self) -> list: 
        return self.__course_pre_request 
    
    def get_course_application(self) -> list: 
        return self.__course_application 
    
    def get_course_outcomes(self) -> list: 
        return self.__course_outcomes 


# **********************************************************
# ********************* Course Unit Data Generator ********* 
# **********************************************************
class CourseUnitData: 

    def __init__(self, unit_data : dict): 
        self.__unit_data = unit_data 
        self.__unit_name = self.__unit_data.get(COURSE_UNIT_NAME)
        self.__unit_des = self.__unit_data.get(COURSE_UNIT_DES)
        self.__unit_link = self.__unit_data.get(COURSE_UNIT_LINK)
        self.__unit_outcomes = self.__unit_data.get(COURSE_UNIT_OUTCOMES)

    def get_unit_name(self) -> str: 
        return self.__unit_name 
    
    def get_unit_des(self) -> str: 
        return self.__unit_des 
    
    def get_unit_links(self) -> list: 
        return self.__unit_link 
    
    def get_unit_outcomes(self) -> list: 
        return self.__unit_outcomes 
    
    

# ************************************************************
# ***************  Course Skill Map **************************
# ************************************************************

class CourseSkillMap: 

    def __init__(self, course_json_extractor : CourseJSONdataExtractor, skill_hot_work_list : list): 
        self.course_json_extractor = course_json_extractor 
        self.skill_hot_word = skill_hot_work_list 
    
    def is_required(self) -> bool: 
        
        ## test subject name. 
        subject_name = self.course_json_extractor.get_subject_name() 
        if find_text(subject_name, self.skill_hot_word): 
            return True 
        
        ## test application list. 
        application_list = self.course_json_extractor.get_course_application()
        for application in application_list: 
            if find_text(application, self.skill_hot_word): 
                return True 
        ## get outcomes list. 
        outcomes_list = self.course_json_extractor.get_course_outcomes()
        for outcomes in outcomes_list: 
            if find_text(outcomes, self.skill_hot_word): 
                return True 
                
        return False 

     
def find_text(input_text : str, target_str_list : list) -> bool:
    for target_str in target_str_list:  
        if input_text.lower().find(target_str.lower()) != -1: 
            return True 
    return False  


def get_tag_course(course_object : CourseData) -> list: 
    tag_course_list = []
    # list of all skils. 
    skill_list = [ skill.domain_name for skill in DomainData.objects.all() ]
    for skill in skill_list: 
        # list of all hot words for that particular skill. 
        skill_word_data_object = SkillHotWords.objects.filter(skill_name = skill)
        skill_list_hot_words = [sk.hot_word for sk in skill_word_data_object]
        if skill_list_hot_words != []: 
            print(skill_list_hot_words)
            skill_map_object = CourseSkillMap(course_json_extractor=CourseJSONdataExtractor(course_json_object=get_json_object_course(course_object)), skill_hot_work_list=skill_list_hot_words)
            if skill_map_object.is_required(): 
                tag_course_list.append(skill)
                

    print("-----------")
    print(tag_course_list)
    print("-----------")
    return tag_course_list 


def get_professor_tag_list(profesor_profile_object : profile): 
    # list of courses by specific profesor. 
    course_list_profesor = [course_data.course_id for course_data in CourseRegisterBy.objects.filter(user_id = profesor_profile_object)]
    # list contan all tag for course. 
    profesor_tag_list = []
    for course in course_list_profesor: 
        # append course tag in profesor tag list. 
        profesor_tag_list.extend(get_tag_course(course_object = course))
    # return tag list profesor. 
    return profesor_tag_list

def get_student_tag_list(student_profile_object : profile): 
    # list of coursed by student. 
    course_list_student = [course_data.course_id for course_data in CourseEnroll.objects.filter(student_id = User.objects.get(username = student_profile_object.user.username))]
    student_tag_list = []
    for course in course_list_student: 
        # append course tag in profesor tag list. 
        student_tag_list.extend(get_tag_course(course_object = course))
    # return tag list profesor. 
    return student_tag_list 
