from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date


todays_date = date.today()

#CHOICES=[("Profesor", "Profesor"), ("Student", "Student")]
SEMESTER=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')]
YEARS=[(i,str(i)) for i in range(todays_date.year,todays_date.year+6)]
BRANCHES=[("CSE", "CSE"), ("CIVIL", "CIVIL"),("ECE", "ECE"),("MECH", "MECH")]
class LoginForm(forms.Form):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    '''username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))'''
    
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))

    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))

    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last name",                
                "class": "form-control"
            }
        ))

    semester = forms.ChoiceField(choices = SEMESTER)
    
    passout_year=forms.ChoiceField(choices=YEARS)

    placement_year=forms.ChoiceField(choices=YEARS)
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirm Password",                
                "class": "form-control"
            }
        ))
   
    
    class Meta:
        model = User
        fields = ('username', 'firstname','lastname','semester','passout_year','placement_year','password1','password2')


class SignUpFormProfessor(UserCreationForm):
    '''username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))'''
    
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))

  
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))

    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last name",                
                "class": "form-control"
            }
        ))
    
   
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirm Password",                
                "class": "form-control"
            }
        ))
   
    Branch = forms.ChoiceField(choices=BRANCHES)
    class Meta:
        model = User
        fields = ('username', 'firstname','lastname', 'password1','Branch','password2')