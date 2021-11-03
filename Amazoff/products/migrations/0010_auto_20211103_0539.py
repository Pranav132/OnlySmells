# Generated by Django 3.2.8 on 2021-11-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ManyToManyField(to='products.Tags'),
        ),
    ]
