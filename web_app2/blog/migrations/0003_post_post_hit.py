# Generated by Django 3.1.5 on 2021-01-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210128_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
