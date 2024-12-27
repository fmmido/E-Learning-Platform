from django.contrib import admin
from .models import Course, Lesson, Enrollment

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1  # Number of empty lesson forms to display

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('title', 'instructor', 'created_at')
    list_filter = ('instructor', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)