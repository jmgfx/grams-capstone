# Generated by Django 2.1.4 on 2019-04-01 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_auto_20190325_0336'),
        ('transactions', '0013_transactions_close_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='vendor',
        ),
        migrations.AddField(
            model_name='transactions',
            name='branch_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin', to='branch.Branch'),
        ),
    ]
