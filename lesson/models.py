from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=15)
    timeout = models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def delete_by_id(id):
        try:
            lesson = Lesson.objects.get(pk=id)
            lesson.delete()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        lessons = Lesson.objects.all()
        return lessons

    @staticmethod
    def get(pk):
        lesson = Lesson.objects.get(pk=pk)
        return lesson
