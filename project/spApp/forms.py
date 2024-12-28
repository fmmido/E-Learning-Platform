from django import forms
from .models import Course, Lesson
from django.contrib.auth.forms import UserCreationForm

# Custom form used for creating users
class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that inherits from Django's UserCreationForm.
     This form adds a required email field to the user creation form.
    """
    email = forms.EmailField(required=True)  # Adds a required email field

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)  # use all fields from the parent form and add email.

# Form for creating and updating courses
class CourseForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Course objects.
    
    This form is based on the Course model and includes fields for title,
     description, instructor and image.
    """
    class Meta:  # Defines the form metadata
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
        fields = ['title', 'content', 'order', 'pdf_material']  # Include your model fields