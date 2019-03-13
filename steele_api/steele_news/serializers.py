from rest_framework import serializers
from .models import NewsStory

class StorySerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.name')
    class Meta:
        
        model = NewsStory
        fields = ('id', 'author_name','headline', 'category','region', 'details', 'date')