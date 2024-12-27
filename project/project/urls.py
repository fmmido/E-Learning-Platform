# your_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# The urlpatterns list defines the URL routes for the entire project
urlpatterns = [
    # This line includes URL patterns from Django's admin app
    # It makes the admin site accessible
    path('admin/', admin.site.urls),

    # This line includes URL patterns from your app's (spApp) urls.py
    # This allows your app's URL definitions to be included in this file.
    path('', include('spApp.urls')), # 'spApp' is your app name
]

# Check if DEBUG mode is enabled in your project's settings
if settings.DEBUG:
    # If the project is running in DEBUG mode
    # This code will serve media files
    # settings.MEDIA_URL is the URL to access your media files (/media/)
    # document_root=settings.MEDIA_ROOT is where the files are located on the server
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)