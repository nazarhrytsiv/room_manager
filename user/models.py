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

    @staticmethod
    def delete_by_id(id):
        try:
            user = User.objects.get(pk=id)
            user.delete()
            return True
        except:
            return False
