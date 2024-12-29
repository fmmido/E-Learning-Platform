FROM python:3.11

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملف المتطلبات من المسار الصحيح
COPY ./project/requirements.txt /app/requirements.txt

# تثبيت المتطلبات (بما في ذلك gunicorn)
RUN pip install --no-cache-dir -r requirements.txt

# تثبيت gunicorn (اختياري، فقط إذا لم يكن موجودًا في requirements.txt)
RUN pip install --no-cache-dir gunicorn
RUN pip install whitenoise

# نسخ ملفات المشروع
COPY ./project /app

# إنشاء مجلدات static و media
RUN mkdir -p /app/media /app/static
RUN chmod -R 777 /app/media /app/static

# تأكد من أن gunicorn يعمل بشكل صحيح
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
