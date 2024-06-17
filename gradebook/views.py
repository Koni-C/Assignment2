from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gradebook.models import Semester, StudentEnrollment, Lecturer, Course, Classroom, Student
from gradebook.serializers import SemesterSerializer, CourseSerializer, LecturerSerializer, ClassroomSerializer, \
    StudentSerializer, StudentEnrollmentSerializer
import pandas as pd
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

@api_view(['GET'])
def index(request):
    course = Course.objects.all()
    serializer = SemesterSerializer(course, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def semester_list(request):
    if request.method == 'GET':
        semester = Semester.objects.all()
        serializer = SemesterSerializer(semester, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = SemesterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
@api_view(['GET', 'PUT', 'DELETE'])
def semester_detail(request, id):
    try:
        semester = Semester.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = SemesterSerializer(instance=semester)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SemesterSerializer(instance=semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        semester.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, id):
    try:
        course = Course.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = CourseSerializer(instance=course)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CourseSerializer(instance=course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        course.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def lecturer_list(request):
    if request.method == 'GET':
        lecturer = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturer, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = LecturerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def lecturer_detail(request, id):
    try:
        lecturer = Lecturer.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = LecturerSerializer(instance=lecturer)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LecturerSerializer(instance=lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        lecturer.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def classroom_list(request):
    if request.method == 'GET':
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = ClassroomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def classroom_detail(request, id):
    try:
        classroom = Classroom.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = ClassroomSerializer(instance=classroom)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ClassroomSerializer(instance=classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        classroom.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = StudentSerializer(instance=student)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        student.delete()
        return Response("Deleted")


@api_view(['GET', 'POST'])
def studentEnrollment_list(request):
    if request.method == 'GET':
        studentEnrollment = StudentEnrollment.objects.all()
        serializer = StudentEnrollmentSerializer(studentEnrollment, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = StudentEnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def studentEnrollment_detail(request, id):
    try:
        studentEnrollment = StudentEnrollment.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = StudentEnrollmentSerializer(instance=studentEnrollment)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudentEnrollmentSerializer(instance=studentEnrollment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == "DELETE":
        studentEnrollment.delete()
        return Response("Deleted")


def download_students_excel(request):
    students = Student.objects.all()
    df = pd.DataFrame(list(students.values()))
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'
    df.to_excel(response, index=False)
    return response

@api_view(['POST'])
def upload_students_excel(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if not file.name.endswith('.xlsx'):
            messages.error(request, 'File is not in Excel format')
            return render(request, 'upload_file.html')

        df = pd.read_excel(file)
        for index, row in df.iterrows():
            student_id = int(row['Student ID'])
            first_name = str(row['First Name'])
            last_name = str(row['Last Name'])
            dob_str = str(row['DOB'])
            dob = datetime.strptime(dob_str.split(' ')[0], '%Y-%m-%d').date()
            email = str(row['email'])

            username = email
            while User.objects.filter(username=username).exists():
                username = email + '_' + str(uuid.uuid4())[:8]  # Append a unique identifier to the username

            user = User.objects.create_user(username=username, email=email)
            student = Student.objects.create(
                student_ID=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                dob=dob,
                user=user
            )

        messages.success(request, 'Students uploaded successfully')
        return render(request, 'upload_file.html')

    return render(request, 'upload_file.html')

def download_students_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="students.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.append(['Student ID', 'First Name', 'Last Name', 'DOB'])

    students = Student.objects.all()
    for student in students:
        ws.append([student.student_ID, student.first_name, student.last_name, student.dob.strftime('%Y-%m-%d')])

    wb.save(response)
    return response

@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        from_email = request.POST.get('from_email')
        to_email = request.POST.get('to_email')

        # Send email
        send_mail(subject, body, from_email, [to_email])
        email_sent = True
    else:
        email_sent = False

    return render(request, 'send_email_out.html', {'email_sent': email_sent})