# Generated by Django 2.1.5 on 2019-01-21 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Brand'),
        ),
    ]