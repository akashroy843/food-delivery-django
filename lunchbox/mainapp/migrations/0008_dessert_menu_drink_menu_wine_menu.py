# Generated by Django 3.1 on 2020-10-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_dinner_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('ingredient', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Drink_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('ingredient', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Wine_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('ingredient', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]
