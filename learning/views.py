from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import *
from django.contrib import messages

def index(request):
    courses = Course.objects.annotate(student_count=Count('enrollment')).order_by('-student_count')
    return render(request, 'learning/index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = Student.objects.filter(enrollment__course=course).order_by('last_name')
    all_students = Student.objects.all()
    
    return render(request, 'learning/course_detail.html', {
    
        'course': course,
        'students': students,
        'all_students': all_students
    })
    
def enroll_student(request):
    
    if request.method == 'POST':
        student_id = request.POST['student']
        course_id = request.POST['course']
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
        
        if not Enrollment.objects.filter(student=student, course=course).exists():
            Enrollment.objects.create(student=student, course=course)
            messages.success(request, f"{student} успешно записан на курс {course}.")
        else:
            messages.error(request, f"{student} уже записан на курс {course}.")

        
        return redirect('course_detail', course_id=course.id)
    
    return redirect('index')