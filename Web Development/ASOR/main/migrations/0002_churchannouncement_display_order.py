# Generated by Django 3.2.7 on 2021-09-28 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchannouncement',
            name='display_order',
            field=models.IntegerField(null=True),
        ),
    ]
