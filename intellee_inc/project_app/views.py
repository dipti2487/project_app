from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from project_app.forms import SignUpForm, EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Contact, Enrollment

def index(request):
    return render(request, 'project_app/home.html')

def home_page(request):
    return render(request, 'project_app/home.html')

def contact_us(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        contact.name=name
        contact.email=email
        contact.comment=comment
        contact.save()
        return HttpResponse("Thank you for your form submission!")
    return render(request, 'project_app/contact.html', {})

def courses(request):
    return render(request, 'project_app/my_course_page.html')

def user_enrollment(request):
    if request.method=="POST":
        enrollment_form=Enrollment()
        name=request.POST.get('name')
        email=request.POST.get('email')
        select_courses=request.POST.get('select_courses')
        enrollment_form.name=name
        enrollment_form.email=email
        enrollment_form.select_courses=select_courses
        enrollment_form.save()
    return render(request, 'project_app/enrollment_form.html', {})

def appointment_date(request):
    return render(request, 'project_app/book_appointment.html')


def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
         messages.success(request, "Account Created Successfully !!")
         fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'project_app/signup.html', {'form':fm})

#Login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'project_app/login.html', {'form': fm})
    else:
         return HttpResponseRedirect('/profile/')

#Profile

def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile Updated!')
                fm.save()
        else:
            fm = EditUserProfileForm(instance = request.user)
        return render (request, 'project_app/profile.html', {'name': request.user, 'form':fm})
    else:
       return HttpResponseRedirect('/login/')


# Create your views here.
#logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Change Password with old Password
def change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change Successfully')
                return HttpResponseRedirect('/profile/')
        else:
          fm = PasswordChangeForm(user = request.user)
        return render(request, 'project_app/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
