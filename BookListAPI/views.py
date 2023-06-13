from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Using functional views for serialization


# Adding the api_view decorator to tell Django that it's an api view and passed an array of allowed HTTP verbs/methods. The combination of api_view decorator and Response method enables the api view interface on the browser.
@api_view(['GET', 'POST'])
def books(request):
    books = Book.objects.all()
    serialized_item = BookSerializer(books, many=True)
    return Response(serialized_item.data, status=status.HTTP_200_OK)


@api_view()
def single_book_view(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serialized_item = BookSerializer(book)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    except:
        return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
