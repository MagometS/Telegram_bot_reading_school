from django.contrib import admin
from django.urls import path
from api.views import LessonView

urlpatterns =[
    path('lessons/all/', LessonView.as_view(), name='all-lessons'),
]