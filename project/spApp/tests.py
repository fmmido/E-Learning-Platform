from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Lesson, Enrollment
from django.core.files.uploadedfile import SimpleUploadedFile


class CourseAppTests(TestCase):
    def setUp(self):
        """Set up for all tests."""
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
         # Create a test staff user
        self.test_staff_user = User.objects.create_user(username = 'teststaff', password='testpassword', is_staff = True)
        # Create a client for making requests
        self.client = Client()


    def test_index_view(self):
      """Test the index view"""
      response = self.client.get(reverse('index'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'index.html')

    def test_signup_view(self):
        """Test the signup view"""
         # Test GET request for signup page
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

        # Test POST request with valid form data
        response = self.client.post(reverse('signup'), {
           'username': 'newuser',
           'email': 'test@test.com',
            'password': 'testpassword',
           'password2': 'testpassword',
       }, follow = True)
        self.assertEqual(response.status_code, 200)  # Expect a 200 after redirecting
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.filter(username='newuser').exists()) # Verify if the user is being created

    def test_signin_view(self):
        """Test the signin view"""
         # Test GET request for signup page
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
        # Test POST request with valid credentials
        response = self.client.post(reverse('signin'), {
           'username': 'testuser',
            'password': 'testpassword',
       }, follow = True)
        self.assertEqual(response.status_code, 200) # Expect a 200 after redirecting
        self.assertRedirects(response, reverse('index'))  # Should redirect to the main page
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # Verify the user was authenticated
    def test_signout_view(self):
        """Test the signout view"""
         # Login user
        self.client.force_login(self.test_user)
        # Test signout endpoint
        response = self.client.get(reverse('signout'), follow=True)
        self.assertEqual(response.status_code, 200) # Expect a 200 after redirecting
        self.assertRedirects(response, reverse('index')) # Should redirect to the main page
        self.assertFalse(response.wsgi_request.user.is_authenticated) # User is not authenticated after signout
    def test_course_list_view(self):
        """Test the course_list view"""
        # test get request
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)  # Assert that page is rendered
        self.assertTemplateUsed(response, 'course_list.html')  # Assert the template is correct
    def test_course_detail_view(self):
        """Test the course_detail view"""
        # create a course for this test
        course = Course.objects.create(title='Test Course', description='Test course description', instructor=self.test_user)
        # Test with existing user
        response = self.client.get(reverse('course_detail', args=[course.id]))
        self.assertEqual(response.status_code, 200) # Assert that page is rendered
        self.assertTemplateUsed(response, 'course_detail.html') # Assert the template is correct
        # Test with non existing course
        response = self.client.get(reverse('course_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)  # Verify that a 404 error is returned
    def test_enroll_course_view(self):
        """Test the enroll_course view"""
         # Create a course and login a user for this test
        course = Course.objects.create(title='Test Course', description='Test course description', instructor=self.test_user)
        self.client.force_login(self.test_user)

        # Test if user can enroll in a course
        response = self.client.get(reverse('enroll_course', args=[course.id]), follow = True)
        self.assertEqual(response.status_code, 200)  # Expect a redirect
        self.assertRedirects(response, reverse('course_detail', args=[course.id]))  # Should redirect to the course page
        self.assertTrue(Enrollment.objects.filter(student=self.test_user, course=course).exists())  # Check that enrollment has been created

        # Test if user cannot enroll in a course twice
        response = self.client.get(reverse('enroll_course', args=[course.id]))
        self.assertEqual(response.status_code, 403)  # expect error 403 forbidden since they are already enrolled

    def test_my_courses_view(self):
        """Test the my_courses view"""
         # Create a course and enroll user for test
        course = Course.objects.create(title='Test Course', description='Test course description', instructor=self.test_user)
        Enrollment.objects.create(student=self.test_user, course=course)
        # Login the user
        self.client.force_login(self.test_user)
         # Test the page is rendered
        response = self.client.get(reverse('my_courses'))
        self.assertEqual(response.status_code, 200)   # assert response code is ok
        self.assertTemplateUsed(response, 'my_courses.html')  # assert correct template is being used
        self.assertContains(response, 'Test Course') # Check that the course that we created and that user enrolled is showing on the response.

    def test_course_create_view(self):
        """Test the course_create view"""
         # Login the staff user
        self.client.force_login(self.test_staff_user)
        # Create a test image file
        image_file = SimpleUploadedFile(name="test.png", content=b"file content", content_type="image/png")
         # Test the form is created using a get request
        response = self.client.get(reverse('course_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_create.html')
          # Test create a course using the form, with data
        response = self.client.post(reverse('course_create'), {
                 'title': 'New Course',
                'description': 'New course description',
                 'instructor': self.test_staff_user.id,
                'image': image_file,
                 'title': 'New Lesson',
                'content': 'New lesson content',
                'order': 1,
             }, follow = True) # follow the redirect
        self.assertEqual(response.status_code, 200)  # expect 200 since we are following redirects
        self.assertRedirects(response, reverse('course_detail', args=[Course.objects.last().id]))  # check if correct redirect
        self.assertEqual(Course.objects.count(), 1)  # check if a course has been added
        self.assertEqual(Lesson.objects.count(), 1) # check if a lesson has been added
        # Test if user is not staff can't see this page
        self.client.force_login(self.test_user)
        response = self.client.get(reverse('course_create'))
        self.assertEqual(response.status_code, 403) # assert returns 403 when user is not staff