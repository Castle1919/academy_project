from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    
    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("Дата окончания курса должна быть позже даты начала.")
    
    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateField(default=timezone.now)
    
    class Meta:
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
    
