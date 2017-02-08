from django import forms

from .models import User

from .models import Teacher


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password')


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('user',)
