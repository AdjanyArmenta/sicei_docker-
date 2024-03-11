from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer
from .models import Student

# Create your views here.

students = [] 
id_counter = 0

def increment_id_counter():
    global id_counter
    id_counter += 1

class StudentListAPIView(APIView):
    def get(self, request):
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

def is_school_id_available(school_id):
    for student in students:
        if student.school_id == school_id:
            return False
    return True

class StudentCreateAPIView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            school_id = serializer.validated_data['school_id']
            if any(student.school_id == school_id for student in students):
                return Response({'error': 'School ID already assigned'}, status=status.HTTP_400_BAD_REQUEST)

            increment_id_counter()
            student_data = serializer.validated_data
            student_data['id'] = id_counter  
            student = Student(**student_data)  
            students.append(student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class StudentDetailAPIView(APIView):  
    def get_object(self,id):
        try:
            return next(student for student in students if student.id == id)  
        except StopIteration:
            raise Http404

    def get(self,request, id):
        student = self.get_object(id)  
        serializer = StudentSerializer(student)  
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)  
        serializer = StudentSerializer(student, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDeleteAPIView(APIView):
    def get_object(self, id):
        try:
            return next(student for student in students if student.id == id)
        except StopIteration:
            raise Http404

    def delete(self, request, id):
        student = self.get_object(id)
        students.remove(student)
        return Response(f"{student.name} deleted",status=status.HTTP_204_NO_CONTENT)

class StudentUpdateAPIView(APIView):
    def get_object(self, id):
        try:
            return next(student for student in students if student.id == id)
        except StopIteration:
            raise Http404

    def put(self, request, id):
        student = self.get_object(id)
        for key, value in request.data.items():
            setattr(student, key, value)
        return Response(StudentSerializer(student).data)





