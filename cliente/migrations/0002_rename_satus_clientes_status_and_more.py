# Generated by Django 4.2.10 on 2024-03-02 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='satus',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='updatef_at',
            new_name='updated_at',
        ),
    ]
