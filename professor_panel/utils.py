from user.models import profile 

class StudentTagMap: 

    def __init__(self, student_profile_data : profile, tag_list_course : list,tag_list_interest : list): 
        self.student_profile = student_profile_data 
        self.tag_list = tag_list_course  
        self.tag_list_in = tag_list_interest
