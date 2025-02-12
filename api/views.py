from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from sqlalchemy import text
from .serializers import DataSerializer
from sqlalchemy_engine import engine

class DataFetchView(APIView):
    def get(self, request):
        query = "SELECT * FROM books"  # Replace with your table name

        with engine.connect() as connection:
            result = connection.execute(text(query))
            data = [dict(row) for row in result]

        serializer = DataSerializer(data, many=True)
        return Response(serializer.data)
