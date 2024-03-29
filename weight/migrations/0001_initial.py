# Generated by Django 2.2.4 on 2019-08-27 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата взвешивания')),
                ('weight', models.FloatField(verbose_name='Вес Мурки в кг')),
                ('comment', models.TextField(verbose_name='Комментарий если надо')),
                ('user', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='Кто добавил')),
            ],
            options={
                'verbose_name': 'Вес',
                'verbose_name_plural': 'Вес',
                'db_table': 'bd_weight',
            },
        ),
    ]
