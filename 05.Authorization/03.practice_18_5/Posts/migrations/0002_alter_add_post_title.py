# Generated by Django 4.2.7 on 2023-12-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_post',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]