# Generated by Django 2.2.16 on 2022-07-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_useranswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(help_text='Текст ответа', max_length=50, verbose_name='Текст'),
        ),
    ]
