# Generated by Django 3.1 on 2021-06-09 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0003_search1_contact1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search1',
            name='Contact1',
        ),
    ]