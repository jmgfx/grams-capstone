# Generated by Django 2.1.4 on 2019-02-20 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetCategories', '0001_initial'),
        ('assets', '0004_auto_20190221_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assetCategories.assetCategory'),
        ),
    ]
