from rest_framework import serializers
from app_bookstore.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = [
            'passed',
            'user_created',
            'date_created',
            'date_updated',
        ]
        read_only_fields = ['id']


class BookSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        exclude = [
            'user_created',
            'date_created',
            'date_updated',
        ]
        read_only_fields = ['id']

    def get_author_first_name(self, obj):
        return obj.author.first_name
    
    def get_author_last_name(self, obj):
        return obj.author.last_name