# Generated by Django 4.1.7 on 2023-03-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0002_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(max_length=14),
        ),
    ]
