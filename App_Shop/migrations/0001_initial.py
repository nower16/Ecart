# Generated by Django 2.2 on 2021-07-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(upload_to='products')),
                ('name', models.CharField(max_length=300)),
                ('preview_text', models.TextField(max_length=200, verbose_name='preview Text')),
                ('detail_text', models.TextField(max_length=1200, verbose_name='Description')),
                ('price', models.FloatField()),
                ('old_price', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='App_Shop.Category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
