from django.contrib import admin
from .models import Author,Article,Review

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Review)
