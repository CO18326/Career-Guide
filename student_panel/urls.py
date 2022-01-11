from django.urls import path
from . import views 

urlpatterns = [
    path('', views.student_panel_home_page, name = "home_page"), 
    path('logout/', views.logout_user, name = "Logout"), 
    path('domainadd/', views.update_domain, name = "DomainUpdate"), 
]
