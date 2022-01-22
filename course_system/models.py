from operator import mod
from django.contrib.auth.models import User 
from django.db import models
from django.db.models.fields.related import ForeignKey
from user.models import profile 

## CourseData contain details of course and course json file. 
class CourseData(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True)
    course_json_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.course_name 

## course register by data contains who as registered the course. 
class CourseRegisterBy(models.Model): 
    course_id = models.ForeignKey(CourseData, on_delete=models.CASCADE,related_name='course_user_map')
    user_id = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='user_course_map')



## Enroll details. 
class CourseEnroll(models.Model): 

    course_id = models.ForeignKey(CourseData, related_name='course_enroll', on_delete=models.CASCADE)
    student_id = models.ForeignKey(User,related_name='student_enroll', on_delete=models.CASCADE)

## Skills Tech Hot Words. 

class SkillHotWords(models.Model): 

    skill_name = models.CharField(max_length=100)
    hot_word = models.CharField(max_length=100)

    def __str__(self): 
        return self.skill_name + "_" + self.hot_word 


class DomainName(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_domain')
    skill_name = models.CharField(max_length=100)

    def __str__(self): 
        return self.skill_name 

class DomainData(models.Model): 
    domain_name = models.CharField(max_length=100)

    def __str__(self): 
        return self.domain_name 

class studentDomain(models.Model): 

    user_id = models.ForeignKey(User, related_name='sudent_d', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)