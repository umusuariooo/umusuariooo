# Generated by Django 4.2.10 on 2024-03-09 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_rename_satus_clientes_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='updated_at',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
