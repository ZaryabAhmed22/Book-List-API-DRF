from django.db import models

# Create your models here.


class Cateogry(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(
        Cateogry, on_delete=models.PROTECT, default=1, null=True)

    class Meta:
        models.Index(fields=['price'])
