# Generated by Django 3.0.8 on 2020-08-29 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200826_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='main_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]