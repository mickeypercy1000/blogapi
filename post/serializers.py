from post.models import Post, Author, Category
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'