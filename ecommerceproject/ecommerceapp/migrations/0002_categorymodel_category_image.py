# Generated by Django 4.1.4 on 2023-01-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='category_image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
