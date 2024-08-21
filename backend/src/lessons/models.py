from django.db import models

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name='Название'
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка'
    )


    def __str__(self) -> str:
        return 'Урок:' + self.title