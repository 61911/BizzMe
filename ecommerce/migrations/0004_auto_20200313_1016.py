# Generated by Django 2.2 on 2020-03-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_auto_20200308_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_1',
            field=models.ImageField(default='default_product.jpg', upload_to='Item_picture'),
        ),
        migrations.AddField(
            model_name='item',
            name='image_2',
            field=models.ImageField(default='default_product.jpg', upload_to='Item_picture'),
        ),
    ]
