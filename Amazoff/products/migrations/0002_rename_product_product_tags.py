# Generated by Django 3.2.4 on 2021-11-17 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='tags',
        ),
    ]
