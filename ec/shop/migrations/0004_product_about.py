# Generated by Django 5.0.1 on 2024-02-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
