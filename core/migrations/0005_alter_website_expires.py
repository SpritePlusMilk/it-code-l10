# Generated by Django 4.2.1 on 2023-05-24 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_client_dns_server_alter_website_expires_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 9, 31, 29, 642085, tzinfo=datetime.timezone.utc)),
        ),
    ]
