from django.urls import path
from . import views 

urlpatterns = [
    path('', views.student_panel_home_page, name = "home_page"), 
    path('list-profesor/', views.professor_list, name = "ProfesorList"), 
    path('logout/', views.logout_user, name = "Logout"), 
    path('domainadd/', views.update_domain, name = "DomainUpdate"), 
    path('enrollcourselist/', views.get_enrolled_course_list, name="EnrollList"),
    path('profesor-course-list/<str:username>',views.get_profesor_course),
    path('student-domain/', views.student_intrest_course_list,name="Dpopup")
]
