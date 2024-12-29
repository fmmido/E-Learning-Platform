FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY ./project/requirements.txt /app/requirements.txt

# Install dependencies (including gunicorn and whitenoise)
RUN pip install --no-cache-dir -r requirements.txt

# Optionally, install gunicorn and whitenoise if not included in requirements.txt
# RUN pip install --no-cache-dir gunicorn
# RUN pip install --no-cache-dir whitenoise

# Copy project files into the container
COPY ./project /app

# Create necessary directories for static and media files
RUN mkdir -p /app/static /app/media

# Set permissions for static and media directories
RUN chmod -R 755 /app/static /app/media /app/staticfiles

COPY ./project/static /app/static

# Copy media files
COPY ./project/media /app/media

# Collect static files for production
RUN python manage.py collectstatic --noinput

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
