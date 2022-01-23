from django.urls import path

from professor_panel.core import get_student_map 
from . import views 

urlpatterns = [
    path('', views.professor_dashboard, name="ProfessorDashboard"), 
    path('logout/', views.professor_logout, name = "ProfessorLogout"),
    path('studentview/', views.student_data_view, name="StudentMap")
]
