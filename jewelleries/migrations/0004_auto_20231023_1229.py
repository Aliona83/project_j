# Generated by Django 3.0.1 on 2023-10-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelleries', '0003_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='review',
            field=models.TextField(max_length=500),
        ),
    ]
