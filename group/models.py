from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30)
    img = models.CharField(max_length=30, default='')
    description = models.TextField(max_length=620)
    captain = models.OneToOneField('user.User', null=True, on_delete=models.SET_NULL, default=None, related_name='User')

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
    def get_all():
        groups = Group.objects.all()
        return groups

    @staticmethod
    def get(pk):
        try:
            return Group.objects.get(pk=pk)
        except:
            return None
