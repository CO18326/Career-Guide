from django.contrib import admin
from .models import CourseData, CourseRegisterBy, CourseEnroll, DomainName, DomainData, studentDomain, SkillHotWords  

admin.site.register(CourseData)
admin.site.register(CourseRegisterBy)
admin.site.register(CourseEnroll)
admin.site.register(DomainName)
admin.site.register(DomainData)
admin.site.register(studentDomain)
admin.site.register(SkillHotWords)