# Generated by Django 2.2.10 on 2021-01-12 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210112_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='roomNumber',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
