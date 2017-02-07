from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=620)
    captain = models.OneToOneField('User', null=True, on_delete=models.SET_NULL, default=None, related_name='User')

    def __str__(self):
        return self.name

    @staticmethod
    def delete_by_id(id):
        try:
            group = Group.objects.get(pk=id)
            group.delete()
            return True
        except:
            return False

    @staticmethod
    def get():
        groups = Group.objects.all()
        return groups


class User(models.Model):
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, default=None)

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


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, default=None)

    def __str__(self):
        return self.user.name
