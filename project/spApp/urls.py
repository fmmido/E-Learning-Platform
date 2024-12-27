from django.urls import path
from . import views

# The urlpatterns list routes URLs to views.
urlpatterns = [
    # This is the URL pattern for the index page
    # When an empty url is requested, Django will call the views.index
    # function and it will be named index
    path('', views.index, name='index'),
    
    # This is the URL pattern for the signup page
    # When the url is '/signup/', Django will call views.signup
    # and it will be named signup.
    path('signup/', views.signup, name='signup'),

    # This is the URL pattern for the signin page
    # When the url is '/signin/', Django will call views.signin
    # and it will be named signin.
    path('signin/', views.signin, name='signin'),

    # This is the URL pattern for the signout page
    # When the url is '/signout/', Django will call views.signout
    # and it will be named signout.
    path('signout/', views.signout, name='signout'),
    
    # This is the URL pattern for the course list page
    # When the url is '/courses/', Django will call views.course_list
    # and it will be named course_list.
    path('courses/', views.course_list, name='course_list'),

    # This is the URL pattern for a course detail page
    # When the url is '/courses/<int:course_id>/', Django will call views.course_detail
    # and pass the integer in the url to the view as course_id, and it will be named
    # course_detail.
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),

    # This is the URL pattern for a lesson detail page
    # When the url is '/courses/<int:course_id>/lessons/<int:lesson_id>/',
    # Django will call views.lesson_detail and pass the integers in the url
    # to the view as course_id and lesson_id, and the pattern will be
    # named lesson_detail
    path('courses/<int:course_id>/lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),

    # This is the URL pattern for enrolling in a course
    # When the url is '/courses/<int:course_id>/enroll/',
    # Django will call views.enroll_course and pass the integer in the url
    # to the view as course_id, and it will be named enroll_course.
    path('courses/<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
    
    # This is the URL pattern for the my courses page
    # When the url is '/my-courses/', Django will call views.my_courses
    # and it will be named my_courses
    path('my-courses/', views.my_courses, name='my_courses'),

    # This is the URL pattern for create course page
    # When the url is '/courses/create/', Django will call views.course_create
    # and it will be named course_create
    path('courses/create/', views.course_create, name='course_create'),
     
      # This is the URL pattern for a test user page
    # When the url is '/test-user/',
    # Django will call views.test_user and it will be named test_user
     path('test-user/', views.test_user, name='test_user')
]