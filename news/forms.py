from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'content', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of article'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of article'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content of article'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date published'
            })
        }
