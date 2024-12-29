# Dockerfile

FROM python:3.11

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملف المتطلبات من المسار الصحيح
COPY ./project/requirements.txt /app/requirements.txt

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ ملفات المشروع
COPY ./project /app

# إنشاء مجلدات static و media
RUN mkdir -p /app/media /app/static
RUN chmod -R 777 /app/media /app/static

CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
