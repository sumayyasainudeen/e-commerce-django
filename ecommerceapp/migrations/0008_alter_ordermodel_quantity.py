# Generated by Django 4.1.4 on 2023-06-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0007_alter_cartmodel_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
