from rest_framework import serializers
from .models import *

class CatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagories
        fields = '__all__'

class StudentDataSerializer(serializers.ModelSerializer):
    catagory = serializers.StringRelatedField(many=False)
    class Meta:
        model = StudentData
        fields = ['linkToProof', 'desc_by_student', 'submissiondate', 'checkedByTeacher', 'catagory']

class StudentSerializer(serializers.ModelSerializer):
    student_data = StudentDataSerializer(many=True)

    class Meta:
        model = Student
        fields = ['fname', 'roll', 'collegeID', 'dept', 'points', 'student_data']