# Generated by Django 4.2.7 on 2023-12-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookCollection', '0003_alter_addbook_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addbook',
            name='category',
        ),
        migrations.AddField(
            model_name='addbook',
            name='category',
            field=models.ManyToManyField(to='bookCollection.category'),
        ),
    ]