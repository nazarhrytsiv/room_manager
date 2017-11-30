from django.db import models


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=10)
    description = models.TextField()
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
    def get_by_id(pk):
        try:
            return  Room.objects.get(pk=pk)
        except:
            return None

    @staticmethod
    def get_by_room_name(room):
        try:
            return Room.objects.get(name=room)
        except:
            return None