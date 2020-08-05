from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()

# Create your models here.

class Mentor(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Catagories(models.Model):
    catName = models.CharField(max_length=500)
    point = models.IntegerField(default=0)
    maxPoints = models.IntegerField()

    def __str__(self):
        return self.catName

class Student(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=50)
    roll = models.CharField(max_length=15, primary_key=True)
    collegeID = models.CharField(max_length=13, null=True)
    dept = models.CharField(max_length=3, null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.fname + " | " + self.roll

class StudentData(models.Model):
    for_student = models.ForeignKey(Student, related_name='student_data', on_delete=models.CASCADE)
    linkToProof = models.CharField(max_length=2000)
    catagory = models.ForeignKey(Catagories, related_name='catagory', on_delete=models.CASCADE)
    desc_by_student = models.TextField(max_length=160)
    submissiondate = models.DateTimeField(auto_now_add=True)
    checkedByTeacher = models.BooleanField(default=False)
    def __str__(self):
        return str(self.catagory) + " | " + str(self.submissiondate)
    

