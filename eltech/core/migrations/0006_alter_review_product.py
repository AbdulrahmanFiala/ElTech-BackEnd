# Generated by Django 4.2.7 on 2023-11-09 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.product'),
        ),
    ]
