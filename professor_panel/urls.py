from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.professor_dashboard, name="ProfessorDashboard"), 
    path('logout/', views.professor_logout, name = "ProfessorLogout")
]
