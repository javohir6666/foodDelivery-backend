# Generated by Django 5.0.7 on 2024-07-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_fooditem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='weight',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
