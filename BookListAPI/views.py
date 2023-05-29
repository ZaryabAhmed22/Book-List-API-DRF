from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Using functional views for serialization


@api_view()
def books(request):
    books = Book.objects.all()
    serialized_item = BookSerializer(books, many=True)
    return Response(serialized_item.data)
