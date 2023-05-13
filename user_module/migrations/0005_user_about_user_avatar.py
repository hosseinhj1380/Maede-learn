# Generated by Django 4.1.2 on 2023-05-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0004_rename_activation_email_user_activation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='درباره شخص'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='', verbose_name='آواتار'),
        ),
    ]
