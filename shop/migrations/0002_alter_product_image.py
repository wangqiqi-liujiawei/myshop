# Generated by Django 4.2.3 on 2023-07-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/products/%Y/%m/%d'),
        ),
    ]
