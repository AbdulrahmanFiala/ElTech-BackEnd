# Generated by Django 4.2.7 on 2023-11-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_weeklydeal_deal_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_thumbnail',
            field=models.BooleanField(default=False),
        ),
    ]
