# Generated by Django 2.2.6 on 2019-10-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('god', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confdb',
            name='confEndDate',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='confdb',
            name='confStartDate',
            field=models.CharField(max_length=120),
        ),
    ]