# Generated by Django 3.1 on 2020-10-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images')),
                ('date', models.DateField()),
                ('uploadby', models.CharField(max_length=100)),
                ('subject', models.TextField()),
            ],
        ),
    ]