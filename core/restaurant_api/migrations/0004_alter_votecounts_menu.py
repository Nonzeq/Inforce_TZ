# Generated by Django 4.0.6 on 2022-07-27 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_api', '0003_alter_menu_menu_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votecounts',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='restaurant_api.menu'),
        ),
    ]
