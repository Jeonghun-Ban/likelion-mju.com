# Generated by Django 3.0.3 on 2020-03-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_application_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='application',
            name='field',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]