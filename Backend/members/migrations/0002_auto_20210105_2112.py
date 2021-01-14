# Generated by Django 2.2.10 on 2021-01-05 21:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='frist_name',
            new_name='cardNumber',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='last_name',
            new_name='cardType',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='mobileNumbe',
            new_name='expiryDate',
        ),
        migrations.AddField(
            model_name='users',
            name='checkIn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='firstName',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='lastName',
            field=models.CharField(default='gggg', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='mobileNumber',
            field=models.CharField(default='ghjk', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='type',
            field=models.CharField(default='yghujik', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='dateOfBirth',
            field=models.CharField(max_length=50),
        ),
    ]
