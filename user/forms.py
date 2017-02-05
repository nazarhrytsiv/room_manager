from django import forms

from .models import User

from .models import Group

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password' , 'group')


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ( 'name', 'description')