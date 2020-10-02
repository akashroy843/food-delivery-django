# Generated by Django 3.1 on 2020-10-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lunch_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('ingredient', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Breakfast_Menu',
        ),
    ]
