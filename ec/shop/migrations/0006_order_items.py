# Generated by Django 5.0.1 on 2024-02-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_alter_contact_phone_alter_product_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
