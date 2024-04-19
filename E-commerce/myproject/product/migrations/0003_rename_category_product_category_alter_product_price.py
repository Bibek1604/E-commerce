# Generated by Django 5.0.1 on 2024-04-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]