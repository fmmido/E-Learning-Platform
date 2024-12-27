from django import forms
from .models import Course, Lesson
from django.contrib.auth.forms import UserCreationForm

# Custom form used for creating users
class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that inherits from Django's UserCreationForm.
    
    This form doesn't add any new fields but provides a place for future customization.
    """
    pass # Does not have additional fields

# Form for creating and updating courses
class CourseForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Course objects.
    
    This form is based on the Course model and includes fields for title,
    description, instructor and image.
    """
    class Meta: # Defines the form metadata
        # Set the model to be based on
        model = Course
        # Defines the fields to use in the form
        fields = ['title', 'description', 'instructor', 'image']  # Include 'title'


# Form for creating and updating lessons
class LessonForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Lesson objects.
    
    This form is based on the Lesson model and includes fields for title, content, and order.
    """
    class Meta:  # Defines the form metadata
        # Set the model to be based on
        model = Lesson
        # Defines the fields to use in the form
        fields = ['title', 'content', 'order']  # Include your model fields