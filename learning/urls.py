from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('enroll/', views.enroll_student, name='enroll_student'),
]
