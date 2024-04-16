from rest_framework import serializers
from .models import Book, BookProgress

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookProgress
        fields = '__all__'
