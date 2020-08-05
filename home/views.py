from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, AnonymousUser

import datetime
from core import models
from . import forms



print(datetime.datetime(2000, 9, 29))
# Create your views here.

def isLoggedIn(user):
    if user.is_authenticated:
        return True
    else:
        return False


class Home(View):
    def get(self, request, *args, **kwargs):
        print(request.user, AnonymousUser())
        loggedIn = isLoggedIn(request.user)
        return render(request, "home/home.html", {'user': 'student', 'sform': StudentLoginPage.sform, 'tform': StudentLoginPage.tform, 'typeOfError': 'd-none', "loggedIn": loggedIn})

    def post(self, request, *args, **kwargs):
        return redirect("/")

    def put(self, request, *args, **kwargs):
        return redirect("/")



class StudentLoginPage(View):
    sform = forms.LoginStudent()
    tform = forms.LoginTeacher()
    def get(self, request, *args, **kwargs):
        if not isLoggedIn(request.user):
            return render(request, 'home/login.html', {
            'sform': self.sform, 
            'tform': self.tform, 
            'typeOfError': 'd-none', 
            'user': 'student'
            })
        else:
            return redirect("/student/dashboard/")
        

    def post(self, request, *args, **kwargs):
        semail = request.POST['semail']
        spassword = request.POST['spassword']

        student_user_object = authenticate(username=semail, password=spassword)
        if student_user_object is not None:
            if student_user_object.is_active:
                try:
                    login(request, student_user_object)
                except Exception:
                    return render(request, 'home/login.html', {
                        'sform': self.sform, 
                        'tform': self.tform, 
                        'error': 'This Email or Password doesnot exists.', 
                        'typeOfError': '', 
                        'user': 'student'
                    })
                return redirect('/student/dashboard/')
            else:
                return render(request, 'home/login.html', {
                        'sform': self.sform, 
                        'tform': self.tform, 
                        'error': 'This Email or Password doesnot exists.', 
                        'typeOfError': '', 
                        'user': 'student'
                    })
        else:
            return render(request, 'home/login.html', {
                'sform': self.sform, 
                'tform': self.tform, 
                'error': 'This Email or Password doesnot exists.', 
                'typeOfError': '', 
                'user': 'student'
                })

class StudentDashboardPage(View):
    @method_decorator(login_required(login_url="/student/login/"))
    def get(self, request, *args, **kwargs):
        loggedIn = isLoggedIn(request.user)
        return render(request, 'home/dashboard.html', {
            'user': 'student', 
            'student': request.user.student, 
            'dept': " ".join(forms.departments[request.user.student.dept].split()[:-1]), 
            'sform': StudentLoginPage.sform, 
            'tform': StudentLoginPage.tform, 
            'typeOfError': 'd-none',
            'loggedIn': loggedIn,
            'itemList': request.user.student.studentdata_set.all(),
            'addItemForm': forms.InsertData()
            })

    @method_decorator(login_required(login_url="/student/login/"))
    def post(self, request, *args, **kwargs):
        return redirect("/student/dashboard/")


class StudentProfilePage(View):
    @method_decorator(login_required(login_url="/student/login/"))
    def get(self, request, *args, **kwargs):
        return render(request, 'home/profile.html', {
            'profileForm' : forms.StudentProfile,
            'editable': 'disabled',
            
        })

class AddStudentData(View):
    @method_decorator(login_required(login_url="/student/login/"))
    def get(self, request, *args, **kwargs):
        return redirect('/student/dashboard/')

    @method_decorator(login_required(login_url="/student/login/"))
    def post(self, request, *args, **kwargs):
        data = request.POST
        request.user.student.studentdata_set.create(catagory=models.Catagories.objects.get(id=data['catagory']), linkToProof=data['link_to_file'], desc_by_student=data['description'])
        return redirect('/student/dashboard/')


def logout_session(request):
    logout(request)
    return redirect("/")




# Handlers
def Error404(request):
    return HttpResponse("ERROR 404")

