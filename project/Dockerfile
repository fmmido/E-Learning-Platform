# Use Python 3.11 base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Upgrade pip and install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Add /usr/local/bin to PATH if it's not already there
ENV PATH="/usr/local/bin:$PATH"

# Copy the application code into the container
COPY . .

# Install Gunicorn
RUN pip install gunicorn

# Set the environment variables for Django settings and secret key
ENV DJANGO_SETTINGS_MODULE=project.settings
ENV SECRET_KEY=${SECRET_KEY}

# Set the static root directory (ensure this is in your settings.py as well)
ENV STATIC_ROOT=/app/staticfiles

# Run collectstatic to gather static files after the code has been copied
RUN python manage.py collectstatic --noinput

# Expose the necessary port
EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "project.wsgi:application"]
