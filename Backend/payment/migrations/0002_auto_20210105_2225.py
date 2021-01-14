# Generated by Django 2.2.10 on 2021-01-05 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20210105_2218'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.Users'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expiryDate',
            field=models.CharField(max_length=50),
        ),
    ]
