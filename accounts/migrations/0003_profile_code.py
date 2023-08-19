# Generated by Django 4.2.2 on 2023-08-19 23:02

from django.db import migrations, models
import utils.generate_code


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(default=utils.generate_code.generate_code, max_length=10),
        ),
    ]