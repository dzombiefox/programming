from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta :
        model =Book
        fields=["title","author","type_of_book","number_of_page","publish_at"]