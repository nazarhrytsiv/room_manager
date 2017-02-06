from django import forms

from .models import User

from .models import Group

from .models import  Teacher

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password' , 'group' )


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ( 'name', 'description')


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ( 'user' , )