# Generated by Django 4.2.1 on 2023-05-29 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("BookListAPI", "0004_remove_book_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="BookListAPI.cateogry",
            ),
        ),
    ]
