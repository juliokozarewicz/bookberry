from django import forms
from .models import booksDataBase

class insertBook(forms.ModelForm):

    class Meta:
        model = booksDataBase

        widgets = {
            'dateRelease': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'datex'}),
            'bookname': forms.TextInput(attrs={'placeholder': 'Insira o nome do livro'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'Insira o ISBN'}),
            'autor': forms.TextInput(attrs={'placeholder': 'Insira o nome do autor'}),
        }

        exclude = ('user',)