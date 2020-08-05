from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, AnonymousUser
# Create your views here.

from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .serializers import StudentSerializer, StudentDataSerializer, CatagoriesSerializer
from .models import Student, StudentData, Catagories




class GetStudentData(APIView):
    permission_classes = (
        IsAuthenticated,
    )

    def get(self, request, *args, **kwargs):
        student = request.user.student
        data = StudentSerializer(student)
        return Response(data.data)

@api_view(['GET'])
def getCatagories(request):
    catagories = Catagories.objects.all()
    catagories_serializer = CatagoriesSerializer(catagories, many=True)
    return Response(catagories_serializer.data)



