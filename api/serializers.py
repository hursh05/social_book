from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    column1 = serializers.CharField(max_length=255)
    column2 = serializers.CharField(max_length=255)
    # Add more fields based on your query result
