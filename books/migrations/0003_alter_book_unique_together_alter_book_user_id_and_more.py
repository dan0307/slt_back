# Generated by Django 4.2 on 2024-04-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='book',
            name='user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('user_id', 'book_id')},
        ),
    ]