from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login_view, name = "login"), 
    path('signup/', views.register_user, name = "register"),
    path('signupProfessor/', views.register_professor, name = "registerProfessor")
]
