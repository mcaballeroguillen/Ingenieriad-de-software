
from django import forms

from .models import Todo


class PostForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('actividad',)
