# Generated by Django 3.2.9 on 2021-12-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_alter_suggest_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggest',
            name='text',
            field=models.TextField(),
        ),
    ]