from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.StudentLoginPage.as_view()),
    path('dashboard/', views.StudentDashboardPage.as_view()),
    path('adddata/', views.AddStudentData.as_view()),
]


