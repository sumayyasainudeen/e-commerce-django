# Generated by Django 4.1.4 on 2023-06-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0005_cartmodel_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
