from __future__ import unicode_literals
import datetime
from django.db import models


# Create your models here.

class Lecture(models.Model):
    lesson = models.ForeignKey('lesson.Lesson', null=True, on_delete=models.SET_NULL, default=None,
                                  related_name='lesson')
    group = models.ForeignKey('group.Group', null=True, on_delete=models.SET_NULL, default=None,
                                 related_name='group')
    room = models.ForeignKey('room.Room', null=True, on_delete=models.SET_NULL, default=None,
                                related_name='room')
    teacher = models.ForeignKey('user.User', null=True, on_delete=models.SET_NULL, default=None,
                                   related_name='teacher')
    number_by_schedule = models.IntegerField(default=1)
    date_time = models.DateTimeField()

    def __str__(self):
        return 'lecture' + str(self.id)

    @staticmethod
    def get_all():
        lectures = Lecture.objects.all()
        return lectures

    def to_dict(self):
        return {
            "title": self.lesson.name,
            "start": self.date_time
        }

    @staticmethod
    def get_by_group(group):
        return Lecture.objects.filter(group=group)

    @staticmethod
    def get_by_id(pk):
        lecture = Lecture.objects.get(pk=pk)
        return lecture

    @staticmethod
    def delete_by_id(id):
        try:
            lecture = Lecture.objects.get(pk=id)
            lecture.delete()
            return True
        except:
            return False