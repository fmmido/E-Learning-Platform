FROM python:3.11

# Set the working directory
WORKDIR /app

COPY ./project/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Optionally, install gunicorn and whitenoise if not included in requirements.txt
# RUN pip install --no-cache-dir gunicorn
# RUN pip install --no-cache-dir whitenoise

COPY ./project /app

RUN mkdir -p /app/static /app/media

RUN chmod -R 755 /app/static /app/media /app/staticfiles


COPY ./project/static /app/static

COPY ./project/media /app/media

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
