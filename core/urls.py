from django.urls import include, path
from .views import GetStudentData, getCatagories

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path("student/", GetStudentData.as_view()),
    path("auth/", obtain_auth_token, name="authenticator"),
    path("catagories/", getCatagories, name="catagories_api")
]
