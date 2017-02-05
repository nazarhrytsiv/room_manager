from django import forms

from .models import User

from .models import Group

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'name', 'surname' , 'email', 'password')


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ( 'name', 'description' , 'members')