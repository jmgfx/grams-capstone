# Generated by Django 2.1.4 on 2019-03-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_auto_20190306_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='projected_life',
            field=models.DurationField(null=True),
        ),
    ]
