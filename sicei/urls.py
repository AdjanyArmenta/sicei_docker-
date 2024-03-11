from django.urls import path
from .views import *

urlpatterns = [
    path('v1/students', StudentListAPIView.as_view(), name='student-list'),
    path('v1/students/create', StudentCreateAPIView.as_view(), name='student-create'),
    path('v1/students/<int:id>', StudentDetailAPIView.as_view(), name='student-detail'),
    path('v1/students/delete/<int:id>', StudentDeleteAPIView.as_view(), name='student-delete'),
    path('v1/students/update/<int:id>', StudentUpdateAPIView().as_view(), name='student-update'),

]