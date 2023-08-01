# Generated by Django 2.2 on 2021-08-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0002_auto_20210730_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(default=True),
        ),
    ]