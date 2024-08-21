from django.shortcuts import render
from api.serializers.lesson_serializer import LessonSerializer
from rest_framework.views import APIView
from lessons.models import Lesson
from rest_framework.response import Response


class LessonView(APIView):

    def get(self, request):
        all_lessons = Lesson.objects.all()
        serialized_lessons = LessonSerializer(all_lessons,many=True)
        return Response(serialized_lessons.data)
