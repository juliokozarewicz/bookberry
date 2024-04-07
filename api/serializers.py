from rest_framework import serializers
from core.models import booksDataBase

class book_serializer(serializers.ModelSerializer):
    class Meta:
        model = booksDataBase
        fields = '__all__'