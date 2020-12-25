from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list,name='students-list'),
    path('student/<int:pk>/',views.student_detail,name='student-detail'),
]