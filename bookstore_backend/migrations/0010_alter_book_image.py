# Generated by Django 4.1 on 2022-08-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_backend', '0009_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/default_book.png', upload_to='upload/'),
        ),
    ]
