# Generated by Django 5.0.2 on 2024-02-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('email', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('zipCode', models.IntegerField(default=0)),
            ],
        ),
    ]
