from django.contrib import admin
from .models import Student, Semester, Course, Lecturer, StudentEnrollment, Classroom

# Register your models here.
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Lecturer)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(StudentEnrollment)

