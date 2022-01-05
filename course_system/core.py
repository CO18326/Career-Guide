# filname : core.py 
# *******************************************************
# **************** Course Json data extractor *********** 
# *******************************************************

from .constants import (
    COURSE_SUBJECT_NAME, 
    COURSE_PRE_REQUEST, 
    COURSE_APPLICATIONS, 
    COURSE_OUTCOMES, 
    COURSE_PATH 
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
        return self.__course_path 

    def get_course_pre_request(self): 
        return self.__course_pre_request 
    
    def get_course_application(self): 
        return self.__course_application 
    
    def get_course_outcomes(self): 
        return self.__course_outcomes 