from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    """Form review"""
    class Meta(Article):
        model = Article
        fields = ('upvotes',)

