# Generated by Django 4.2.7 on 2023-12-12 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50, verbose_name='Task Title')),
                ('taskDescription', models.TextField(verbose_name='Description')),
                ('is_completed', models.BooleanField(default=False)),
                ('TaskAssignDate', models.DateField(default=datetime.date.today, verbose_name='Assigning Date')),
            ],
        ),
    ]
