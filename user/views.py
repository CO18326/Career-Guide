from django.shortcuts import render,redirect
from .forms import LoginForm, SignUpForm,SignUpFormProfessor
from django.contrib.auth import authenticate, login
from .models import profile

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "users/user_login_page.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            a=form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            obj=profile.objects.create(user=a,organisation='Student',branch='CSE',semester=form.cleaned_data.get("semester"),passout_year=form.cleaned_data.get("passout_year"),placement_year=form.cleaned_data.get("placement_year"),firstname=form.cleaned_data.get("firstname"),lastname=form.cleaned_data.get("lastname"))
            obj.save()
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created'
            success = True
            
            #return redirect("/login/")

        else:
            print(form.errors)
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "users/user_signup_page.html", {"form": form, "msg" : msg, "success" : success })


def register_professor(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpFormProfessor(request.POST)
        if form.is_valid():
            a=form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            obj=profile.objects.create(user=a,organisation='Profesor',branch=form.cleaned_data.get("Branch"),firstname=form.cleaned_data.get("firstname"),lastname=form.cleaned_data.get("lastname"))
            obj.save()
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpFormProfessor()

    return render(request, "users/user_signup_professor.html", {"form": form, "msg" : msg, "success" : success })