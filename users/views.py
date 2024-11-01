from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, login,authenticate,logout
from .forms import Login_form,Signup_form
from .models import User

# Create your views here.
def login_view(request):
    login_form=Login_form()
    if request.method=='POST':
        login_form = Login_Form(request=request, data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data["username"],
                password=login_form.cleaned_data["password"],
            )
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form=Login_form()
    return render(request=request, 
                  template_name='users/login.html',
                  context={"login_form":login_form})

def logout_view(request):
    logout(request)
    return redirect("/")

def signup_view(request):
    signup_form=Signup_form()
    if request.method=='POST':
        signup_form=Signup_form(request.POST)
        if signup_form.is_valid:
            signup_form.save()
            return redirect("/login")
        else:
            signup_form=Signup_form()
    return render(request, 'users/signup.html', {'signup_form':signup_form})




        
   

