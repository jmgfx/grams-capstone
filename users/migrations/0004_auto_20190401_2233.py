# Generated by Django 2.1.4 on 2019-04-01 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190401_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='branch.Branch'),
        ),
    ]