from django.urls import path
from . views import StudentList, StudentDetail

urlpatterns = [
    path('',StudentList.as_view(),name='students-list'),
    path('student/<int:pk>/',StudentDetail.as_view(),name='student-detail'),
]