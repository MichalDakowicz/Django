# Generated by Django 5.1.1 on 2024-10-07 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_employee_is_manager_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='employee',
            new_name='employees',
        ),
    ]
