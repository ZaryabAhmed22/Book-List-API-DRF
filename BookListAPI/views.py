from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# Using the APIView


class BookView(APIView):
    def get(self, request):
        # Getting the query params
        # api/books?author=Mike
        author = request.GET.get("author")
        if (author):
            return Response({"message": f"list of books by {author}"}, status=status.HTTP_200_OK)
        return Response({"message": "list of all books"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "a new book created"}, status=status.HTTP_201_CREATED)


class SingleBook(APIView):
    def get(self, request, book_id):
        return Response({"message": f"single book with id {str(book_id)}"}, status=status.HTTP_200_OK)

    def put(self, request, book_id):
        return Response({"title": request.data.get('title')}, status=status.HTTP_200_OK)


# Using generic views to create class based views. The most basic building blocks of a generic class based view are queryset and serializer class


class BookViewGeneric(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
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
