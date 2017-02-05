from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField()
    members = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def delete_by_id(id):
        try:
            room = User.objects.get(pk=id)
            room.delete()
            return True
        except:
            return False