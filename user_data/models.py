from django.db import models
from django.contrib.auth.models import User 

############################################################################ 
### This Application contain all data of Student and Subject. 
### Models name in order are defined below. 
## 1. StudentModel 
############################################################################


class StudentModel(models.Model): 
    user_id = models.ForeignKey(User, related_name='student_user', on_delete=models.CASCADE)
    student_fullname = models.CharField(max_length=200)
    college_name = models.CharField(max_length=200)
    current_year_of_study = models.CharField(max_length=10)
    expected_year_of_passing_out = models.IntegerField()
    expected_year_of_sitting_for_placement = models.IntegerField()

    def __str__(self): 
        return self.student_fullname + "_" + self.college_name 



