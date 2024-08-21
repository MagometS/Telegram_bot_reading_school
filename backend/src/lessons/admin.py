from django.contrib import admin
from lessons.models import Lesson
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'title',
        'link'
    ]

admin.register(Lesson, LessonAdmin)