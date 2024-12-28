from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    """Model representing a course."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    """Model representing a lesson within a course."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField()
    pdf_material = models.FileField(upload_to='lesson_pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    """Model representing student enrollment in a course."""
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollment_set')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='enrollment_set')
    enrollment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"