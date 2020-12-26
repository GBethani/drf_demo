from django.urls import path,include
from . views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students',StudentViewSet)

urlpatterns = [
    path('',include(router.urls))
]

'''
urlpatterns = [
    path('',StudentList.as_view(),name='students-list'),
    path('student/<int:pk>/',StudentDetail.as_view(),name='student-detail'),
]
'''