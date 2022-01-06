# filname : core.py 
# *******************************************************
# **************** Course Json data extractor *********** 
# *******************************************************

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

class CourseJSONdataExtractor: 

    def __init__(self, course_json_object : dict):
        self.__course_json_object = course_json_object 
        # initlize required data 
        self.__subject_name = self.__course_json_object.get(COURSE_SUBJECT_NAME)
        self.__course_path = self.__course_json_object.get(COURSE_PATH)
        self.__course_pre_request = self.__course_json_object.get(COURSE_PRE_REQUEST)
        self.__course_outcomes = self.__course_json_object.get(COURSE_OUTCOMES)
        self.__course_application = self.__course_json_object.get(COURSE_APPLICATIONS)
    
    def get_subject_name(self): 
        return self.__subject_name 

    def get_course_path(self): 

        course_path_keys = list(self.__course_path.keys())
        course_unit_list = []
        for unit in course_path_keys: 
            course_unit_list.append(CourseUnitData(self.__course_path.get(unit)))

        return course_unit_list  

    def get_course_pre_request(self): 
        return self.__course_pre_request 
    
    def get_course_application(self): 
        return self.__course_application 
    
    def get_course_outcomes(self): 
        return self.__course_outcomes 


class CourseUnitData: 

    def __init__(self, unit_data : dict): 
        self.__unit_data = unit_data 
        self.__unit_name = self.__unit_data.get(COURSE_UNIT_NAME)
        self.__unit_des = self.__unit_data.get(COURSE_UNIT_DES)
        self.__unit_link = self.__unit_data.get(COURSE_UNIT_LINK)
        self.__unit_outcomes = self.__unit_data.get(COURSE_UNIT_OUTCOMES)

    def get_unit_name(self): 
        return self.__unit_name 
    
    def get_unit_des(self): 
        return self.__unit_des 
    
    def get_unit_links(self): 
        return self.__unit_link 
    
    def get_unit_outcomes(self): 
        return self.__unit_outcomes 
    
    
        