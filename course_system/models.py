from django.contrib.auth.models import User 
from django.db import models
from django.db.models.fields.related import ForeignKey

class CourseData(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True)
    course_json_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.course_name 


class CourseRegisterBy(models.Model): 
    course_id = models.ForeignKey(CourseData, on_delete=models.CASCADE,related_name='course_user_map')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_course_map')
