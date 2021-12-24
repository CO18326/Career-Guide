from django.db import models

from django.db import models

class CourseData(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, blank=True)
    course_json_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.course_name 

