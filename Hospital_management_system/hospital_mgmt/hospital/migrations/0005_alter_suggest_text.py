# Generated by Django 3.2.9 on 2021-12-11 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_rename_contact_suggest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggest',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
