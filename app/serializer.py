from rest_framework import serializers
from app.models import BookModel
class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields='__all__'