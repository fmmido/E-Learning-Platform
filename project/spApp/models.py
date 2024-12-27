from django.db import models
from django.contrib.auth.models import User

# Course model to represent the courses
class Course(models.Model):
    """Model representing a course."""
    # Title of the course as a CharField
    title = models.CharField(max_length=255)  # Ensure this matches your field

    # Description of the course as a TextField
    description = models.TextField()

    # Instructor of the course, related to the User model
    # When the user is deleted then the courses are also deleted.
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    # Image of the course as an ImageField
    # It can be null and blank. It's stored in 'course_images/' folder.
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Example field

    # Created at time
    created_at = models.DateTimeField(auto_now_add=True)

    # String representation of the course (used for admin panel)
    def __str__(self):
        """Returns the title of the course as string."""
        return self.title

# Lesson model to represent the lessons in a specific course
class Lesson(models.Model):
    """Model representing a lesson within a course."""
    # The course to which the lesson belongs to
    # related_name is used to make it easier to access this related objects
    # When the course is deleted then the lessons are also deleted.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    # Title of the lesson
    title = models.CharField(max_length=200)

    # Content of the lesson
    content = models.TextField()

    # Order of the lesson
    order = models.IntegerField()

    # String representation of the lesson
    def __str__(self):
        """Returns the title of the lesson as string."""
        return self.title

# Enrollment model to keep track of students that have enrolled in courses
class Enrollment(models.Model):
    """Model representing student enrollment in a course."""
    # The student that is enrolling in the course. related_name to get enrollments of student easily.
    # When the student is deleted the enrollments are also deleted
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollment_set')

    # The course to which student enrolled. related_name to get enrollments of courses easily.
    # When the course is deleted the enrollments are also deleted.
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='enrollment_set')

    # Date when the user was enrolled in the course
    enrollment_date = models.DateTimeField(auto_now_add=True)

    # String representation of the enrollment
    def __str__(self):
        """Returns a string indicating the user and the course enrolled."""
        return f"{self.student.username} enrolled in {self.course.title}"