from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson, Enrollment
from django.http import HttpResponseForbidden
from .forms import CourseForm, LessonForm, CustomUserCreationForm


def index(request):
    """Renders the index page.
    
    This view simply renders the 'index.html' template.
    """
    courses = Course.objects.all() # Get all the courses from the database
    return render(request, 'index.html',{'courses': courses}) # renders index page

def signup(request):
    """Handles user registration.
    
    This view handles user signup through a custom user creation form.
    It also logs the user in automatically after successful signup.
    """
    if request.method == 'POST':  # Check if the form has been submitted
        form = CustomUserCreationForm(request.POST)  # Create a form with the data from the post request
        if form.is_valid(): # Check if the form is valid
            user = form.save()   # Save the form data
             # set email for user
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)  # Log the user in
            return redirect('index')  # Redirect to the home page after successful signup
    else:
        form = CustomUserCreationForm()  # If not a post request we create a new form
    return render(request, 'signup.html', {'form': form}) # render the signup page with the form

def signin(request):
    """Handles user login.
    
    This view handles user login via Django's AuthenticationForm.
    If the form is valid, it authenticates the user and logs them in.
    """
    if request.method == 'POST':   # If the request is a post request
        form = AuthenticationForm(request, data=request.POST)  # Create the form to handle login
        if form.is_valid():  # If form is valid
            username = form.cleaned_data.get('username') # Get the username from the cleaned form data
            password = form.cleaned_data.get('password') # Get the password from the cleaned form data
            user = authenticate(username=username, password=password)   # Authenticate the user
            if user is not None: # If user exists
                login(request, user) # Login the user
                return redirect('index')   # Redirect the user to home page
    else:
        form = AuthenticationForm()  # Create a new form if not a POST request
    return render(request, 'signin.html', {'form': form})   # We render the signin template with the default form

def signout(request):
    """Handles user logout.
    
    This view logs the user out and redirects them to the index page.
    """
    logout(request)  # Logout the user
    return redirect('index')  # Redirect to the home page

def course_list(request):
    """Displays a list of all courses for all users.
    
    This view retrieves all courses from the database and passes them to a
    template for rendering.
    """
    query = request.GET.get('q')   # Get the value of 'q' from the URL parameters
    if query:
        courses = Course.objects.filter(title__icontains=query)
    else:
        courses = Course.objects.all() # Get all the courses from the database
    return render(request, 'course_list.html', {'courses': courses})  # render the course list page with the list of courses

def course_detail(request, course_id):
    """Displays details of a specific course.
    
    This view retrieves a specific course by ID and its related lessons.
    It also checks if the user is enrolled in the course.
    """
    course = get_object_or_404(Course, id=course_id)   # Get the course by it's id or return 404 if not found
    lessons = Lesson.objects.filter(course=course).order_by('order')    # Get all the lessons related to the course and order by the order field

    is_enrolled = False # We start assuming that the user is not enrolled.
    if request.user.is_authenticated:   # If the user is logged in, then we check if it's enrolled.
      is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()  # This returns a boolean

    return render(request, 'course_detail.html', {'course': course, 'lessons': lessons, 'is_enrolled': is_enrolled})  # We add the variable here.

def lesson_detail(request, course_id, lesson_id):
    """Displays details of a specific lesson within a course.
    
    This view retrieves a specific lesson by ID related to a specific course,
    and pass it to the template
    """
    course = get_object_or_404(Course, id=course_id)    # Get the course by it's id or return 404 if not found
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)  # Get the lesson by it's id or return 404 if not found
    return render(request, 'lesson_detail.html', {'course': course, 'lesson': lesson})   # Render the lesson detail template

@login_required # If the user is not logged in redirect them to the login page.
def enroll_course(request, course_id):
    """Handles student enrollment in a course.
    
    This view allows a user to enroll in a specific course. It first checks
    if the user is already enrolled to avoid duplicated enrollments.
    """
    course = get_object_or_404(Course, id=course_id)    # Get the course by it's id or return 404 if not found
    # Check if already enrolled
    if Enrollment.objects.filter(student=request.user, course=course).exists():    # Check if there is an enrollment with the current user and the current course
        return HttpResponseForbidden("You are already enrolled in this course.") # Return 403 if user is already enrolled

    Enrollment.objects.create(student=request.user, course=course)   # Create a new enrollment with the user and the course
    return redirect('course_detail', course_id=course_id)  # Redirect to the course detail

@login_required # If the user is not logged in redirect them to the login page.
def my_courses(request):
    """Displays a list of courses in which the user is enrolled.
    
    This view retrieves a list of enrollments related to the current logged-in user
    and displays them.
    """
    enrollments = Enrollment.objects.filter(student=request.user)   # Get all the enrollments of the user
    return render(request, 'my_courses.html', {'enrollments': enrollments})  # render the my_courses template with the list of enrollments

@login_required # If the user is not logged in redirect them to the login page.
def course_create(request):
    """
    Handles the creation of a new course, and also the first lesson of the course.
    
    This view is only available to staff users. It allows creating a course
    and the first lesson in the same form, both of which have their own model.
    """
    if not request.user.is_staff: # Checks if the user has staff permission
        return HttpResponseForbidden("You must be an instructor to create a course.")  # if user is not staff returns 403 error

    if request.method == 'POST':   # Check if the request is a post request
        course_form = CourseForm(request.POST, request.FILES)    # Create the form for the course and gets the data for it and the files (images)
        lesson_form = LessonForm(request.POST, request.FILES)    # Create the form for the lesson and gets the data from it
        
        if course_form.is_valid() and lesson_form.is_valid(): # If the course form is valid and lesson form is also valid
            course = course_form.save(commit=False) # Get the course data and but not save it yet
            course.instructor = request.user   # Save the logged-in user as the instructor
            course.save()   # Save the course data to the database

            lesson = lesson_form.save(commit=False) # Get the lesson data but not save it yet
            lesson.course = course  # set the course as the course related to the lesson
            lesson.save()   # Save the lesson data

            return redirect('course_detail', course_id=course.id)   # Redirect to the course detail page
    else:  # If the request is not post then render the form
        course_form = CourseForm()    # create a new form
        lesson_form = LessonForm()    # create a new form

    return render(request, 'course_create.html', {'course_form': course_form, 'lesson_form': lesson_form}) # render the template with both forms.

def test_user(request):
    """
    A simple view to test the user's authentication status and if it's a staff user.
    
    This view returns the user status and if the user is a staff member in a
    test page.
    """
    return render(request, 'test_user.html', {'user': request.user, 'is_staff': request.user.is_staff})  # renders the test_user template and send the user and is_staff data