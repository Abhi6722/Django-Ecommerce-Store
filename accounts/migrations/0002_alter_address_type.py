# Generated by Django 4.2.2 on 2023-08-19 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(choices=[('Home', 'Home'), ('Office', 'Office'), ('Bussines', 'Bussines'), ('Academy', 'Academy'), ('Other', 'Other')], max_length=10),
        ),
    ]