from .models import Book, Cateogry
from rest_framework import serializers
from decimal import Decimal


class BookSerializer(serializers.ModelSerializer):
    price_after_tax = serializers.SerializerMethodField(
        method_name="calculate_tax")
    category = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ["id", "author", "price",
                  "title", "price_after_tax", "category"]

    def calculate_tax(self, product: Book):
        return product.price * Decimal(1.1)
