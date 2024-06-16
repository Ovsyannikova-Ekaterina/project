#   users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Student, Parent


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')


class StudentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=Parent.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Parent',
        empty_label="Select Parent"
    )

    class Meta:
        model = Student
        fields = ['user', 'birth_date', 'email', 'parent']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Parent.objects.all()
        self.fields['parent'].label_from_instance = lambda obj: f"{obj.user.username} - {obj.user.get_full_name()}"
