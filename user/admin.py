from django.contrib import admin
from .models import User
from .models import Group
from .models import Teacher
# Register your models here.

admin.site.register(User)
admin.site.register(Group)
admin.site.register(Teacher)