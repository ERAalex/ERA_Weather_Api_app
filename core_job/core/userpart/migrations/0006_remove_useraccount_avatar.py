# Generated by Django 4.2.2 on 2023-06-29 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpart', '0005_alter_useraccount_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='avatar',
        ),
    ]
