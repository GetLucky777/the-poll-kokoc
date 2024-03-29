# Generated by Django 2.2.16 on 2022-07-18 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220718_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='color',
            field=models.CharField(choices=[('secondary', 'Черный'), ('primary', 'Синий'), ('danger', 'Красный'), ('success', 'Зеленый')], help_text='Цвет', max_length=20, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='color',
            field=models.ForeignKey(help_text='Приобретаемый цвет', on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='polls.Colors', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='type',
            field=models.CharField(choices=[('login', 'Рамка логина'), ('backgrnd', 'Бэкграунд')], help_text='Предмет покупки', max_length=15, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(help_text='Пользователь', on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
