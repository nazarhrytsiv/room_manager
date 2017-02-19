from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    group = models.ForeignKey('group.Group', null=True, on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return self.username

    @staticmethod
    def delete_by_id(id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        users = User.objects.all()
        return users

    @staticmethod
    def get(pk):
        user = User.objects.get(pk=pk)
        return user
