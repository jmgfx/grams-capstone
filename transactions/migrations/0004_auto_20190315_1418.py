# Generated by Django 2.1.4 on 2019-03-15 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20190301_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='branch_origin',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='schedule',
        ),
        migrations.AddField(
            model_name='transactions',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transactions',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
