# Generated by Django 2.2.4 on 2019-10-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Код авторизации'),
        ),
    ]
