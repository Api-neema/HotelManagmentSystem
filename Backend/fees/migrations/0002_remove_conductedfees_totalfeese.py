# Generated by Django 2.2.10 on 2021-01-05 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conductedfees',
            name='totalFeese',
        ),
    ]
