from django.urls import path 
from . import views 

urlpatterns = [
    path('register/', views.register_course, name = "CourseRegister"), 
    path('viewlist/', views.show_register_course, name = "ShowCourse"),
    path('courseview/<int:course_id>', views.view_coures_coures_id, name = "ViewCourseData"),
    path('enroll/<int:course_id>', views.student_course_enroll, name = "EnrollStudent"), 
]