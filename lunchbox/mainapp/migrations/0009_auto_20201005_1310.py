# Generated by Django 3.1 on 2020-10-05 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_dessert_menu_drink_menu_wine_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': '3. Blogs'},
        ),
        migrations.AlterModelOptions(
            name='breakfast_menu',
            options={'verbose_name_plural': '4. Breakfast_Menus'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': '1. Contacts'},
        ),
        migrations.AlterModelOptions(
            name='dessert_menu',
            options={'verbose_name_plural': '7. Dessert_Menus'},
        ),
        migrations.AlterModelOptions(
            name='dinner_menu',
            options={'verbose_name_plural': '6. Dinner_Menus'},
        ),
        migrations.AlterModelOptions(
            name='drink_menu',
            options={'verbose_name_plural': '9. Drink_Menus'},
        ),
        migrations.AlterModelOptions(
            name='lunch_menu',
            options={'verbose_name_plural': '5. Lunch_Menus'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name_plural': '2. Reservations'},
        ),
        migrations.AlterModelOptions(
            name='wine_menu',
            options={'verbose_name_plural': '8. Wine_Menus'},
        ),
    ]