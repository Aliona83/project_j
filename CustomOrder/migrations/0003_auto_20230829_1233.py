# Generated by Django 3.2.20 on 2023-08-29 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('CustomOrder', '0002_auto_20230829_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customjewellerydesign',
            name='user',
        ),
        migrations.AddField(
            model_name='customjewellerydesign',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_forms', to='profiles.userprofile'),
        ),
    ]
