# Generated by Django 2.2.16 on 2022-07-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20220717_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='color',
            field=models.CharField(choices=[('BLACK', 'BLACK'), ('BLUE', 'BLUE'), ('RED', 'RED'), ('GREEN', 'GREEN')], max_length=10),
        ),
    ]