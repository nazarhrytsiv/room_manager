from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10)
    desription = models.TextField()
    size = models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def delete_by_id(id):
        try:
            room = Room.objects.get(pk=id)
            room.delete()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        rooms = Room.objects.all()
        return rooms

    @staticmethod
    def get(pk):
        room = Room.objects.get(pk=pk)
        return room
