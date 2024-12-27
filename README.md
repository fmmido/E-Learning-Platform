# E-Learning Platform

This is a Django-based E-Learning platform that allows users to browse, enroll in, and manage online courses. It provides user authentication, course creation, lesson management, and student enrollment capabilities.

## Features

*   **User Authentication:** Secure registration and login using Django's built-in authentication system.
*   **Course Browsing:** Public listing of available courses.
*   **Course Detail:** Detailed information on each course, including lessons.
*   **Lesson Display:** Detailed view of individual lessons within a course.
*   **Student Enrollment:** Users can enroll in courses.
*   **My Courses:** Logged-in users can view their enrolled courses.
*   **Course Creation:** Instructors (staff users) can create new courses and their first lesson using forms.
*   **Responsive Design:** Basic design that adapts to different screen sizes.

## Project Structure
your_project/
your_project/ # Main project directory
settings.py # Django settings file
urls.py # Project-level URL configurations
wsgi.py # WSGI configuration
...
spApp/ # Django app directory
migrations/ # Database migrations
models.py # Django models for database
views.py # Django views for handling requests
urls.py # App-level URL configurations
forms.py # Django forms for input
templates/ # HTML templates
static/ # Static files (CSS, JavaScript, Images)
css/
styles.css
js/
images/
...
media/ # Media files for user uploaded content (images)
course_images/
...
db.sqlite3 # Database file
manage.py # Django management script

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/fmmido/E-Learning-Platform.git
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: SDP\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    *If you do not have a requirements.txt, make one by using `pip freeze > requirements.txt`*
4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Key Files

*   **`your_project/settings.py`**: Contains all Django settings and project configuration.
*   **`your_project/urls.py`**: Manages project level URL routing.
*   **`spApp/models.py`**: Defines the database models (Course, Lesson, Enrollment).
*   **`spApp/views.py`**: Contains the view functions for handling HTTP requests.
*   **`spApp/urls.py`**: Manages app level URL routing.
*   **`spApp/forms.py`**: Defines the forms used for user input (e.g. signup, course creation and login).
*   **`spApp/templates/`**: Contains all the HTML templates for the pages.
*   **`spApp/static/`**: Holds static files like css (styles.css) , JavaScript, and images.
*   **`media/`**: Holds user-uploaded media files.

## Models

*   **Course:** Represents a course and includes fields like `title`, `description`, `instructor` (User), `image`, and `created_at`.
*   **Lesson:** Represents a lesson inside a course, and includes fields like `title`, `content`, `order`, and a ForeignKey to a `Course`.
*   **Enrollment:** Represents a user enrolling in a course, has a ForeignKey to a `User` and to a `Course`.

## Views

*   `index()`: Main landing page.
*   `signup()`: Handles user registration.
*   `signin()`: Handles user login.
*   `signout()`: Handles user logout.
*   `course_list()`: Lists all courses.
*   `course_detail(course_id)`: Shows details of a specific course.
*   `lesson_detail(course_id, lesson_id)`: Displays details of a specific lesson.
*   `enroll_course(course_id)`: Allows users to enroll in a course.
*   `my_courses()`: Shows courses a logged-in user is enrolled in.
*   `course_create()`: Allows staff users to create new courses and first lessons.
*    `test_user()`: a simple view for testing user authentication status.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature`).
3.  Make your changes.
4.  Commit your changes (`git commit -am 'Add your feature'`).
5.  Push the branch (`git push origin feature/your-feature`).
6.  Create a new Pull Request.

## License

This project is licensed under the MIT.

## Acknowledgements

*   [List of packages, dependencies or inspirations]
*  [People if any were involved].

## Contact

If you have any questions, feel free to contact.

How to Use:

Copy: Copy the Markdown content above.

Create README: Create a file named README.md (note the extension) in the root directory of your Git repository.

Paste: Paste the content into your README.md file.

Customize: Customize the [Your email], [Your username], [your-repo-name], [List of packages, dependencies or inspirations], and [People if any were involved] sections to reflect your project details.

Commit: Commit and push the README.md file to your repository.
