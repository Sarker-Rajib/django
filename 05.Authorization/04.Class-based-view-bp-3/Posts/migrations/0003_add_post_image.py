# Generated by Django 4.2.7 on 2023-12-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_alter_add_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]