# Generated by Django 4.2 on 2023-05-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acctholders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acctholders',
            name='aadhaar',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='acctholders',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
