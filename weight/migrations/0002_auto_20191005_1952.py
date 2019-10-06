# Generated by Django 2.2.4 on 2019-10-05 16:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий если надо'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата взвешивания'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Кто добавил'),
        ),
    ]
