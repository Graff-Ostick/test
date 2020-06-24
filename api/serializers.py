from rest_framework import serializers
from .models import Article, Review

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ReviewSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'