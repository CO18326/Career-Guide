from django.urls import path 
from . import views 

urlpatterns = [
    path('register/', views.register_course, name = "CourseRegister"), 
    path('viewlist/', views.show_register_course, name = "ShowCourse")
]