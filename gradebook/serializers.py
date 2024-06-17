from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from gradebook.models import Semester, StudentEnrollment, Lecturer, Course, Classroom, Student

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['year', 'semester_number', 'id']

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']
        # fields = "__all__"

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_code', 'course_name', 'semesters']


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'staff_ID', 'first_name', 'last_name', 'email', 'courses', 'dob']

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'classroom_number', 'semester', 'course', 'lecturer']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_ID', 'first_name', 'last_name', 'email', 'dob']

class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = ['id', 'student_ID', 'class_enrolled', 'grade', 'enroll_time', 'grade_time']