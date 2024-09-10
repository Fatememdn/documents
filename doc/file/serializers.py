from rest_framework import serializers
from .models import TextFile

class TextFileCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFile
        fields = ['file']
    def validate_file(self, value):
        if not value.name.endswith('.txt'):
            raise serializers.ValidationError("Only .txt files are allowed.")
        return value

class TextFileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFile
        fields = ['id', 'file',  'created_at', 'updated_at']
