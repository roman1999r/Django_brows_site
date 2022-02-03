import re

from django import forms
from .models import *

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'photo', ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
            # 'photo': forms.ImageField(upload_to='photos/%Y/%m/%d/', blank=True),
        }


class PhotoForm(forms.ModelForm):
    class Meta:
        model = WorkPhotos
        fields = ['title', 'content', 'category', 'photo', ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match(r'\d', title):
                raise ValidationError('Название не должно начинаться с цифры')
            return title


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'start_date', 'end_time', 'name', 'number', 'instagram', 'email']
        widgets = {
            'title': forms.Select(attrs={"class": "form-control"}),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'class': 'myTimeClass', 'placeholder': 'Select a time'}),
            'start_date': forms.DateInput(format='%d-%m-%Y', attrs={'class': 'myDateClass', 'placeholder': 'Select a date'}),
            'end_time': forms.HiddenInput,
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'number': forms.TextInput(attrs={"class": "form-control"}),
            'instagram': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
