## Parse Course json fiele and get required data. 

class CourseJSONParse: 

    def __init__(self, json_object): 
        self.__course_name = json_object.get('subject_name')
        self.__course_pre = json_object.get('pre')
        self.__course_path = json_object.get('path')
        self.__course_outcome = json_object.get('outcome')

    def course_name(self): 
        return self.__course_name 
        
    def get_pre(self): 
        return self.__course_pre

    def get_path(self): 
        return self.__course_path

    def get_outcome(self): 
        return self.__course_outcome 
    
    def get_levels_list(self): 
        self.__course_level_list = []
        for key in self.__course_path.keys(): 
            self.__course_level_list.append(self.__course_outcome.get(key))
        return self.__course_level_list 
    

