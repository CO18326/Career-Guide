from django.contrib import admin
from .models import CourseData, CourseRegisterBy, CourseEnroll 

admin.site.register(CourseData)
admin.site.register(CourseRegisterBy)
admin.site.register(CourseEnroll)