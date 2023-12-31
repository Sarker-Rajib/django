# Generated by Django 4.2.7 on 2023-12-24 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/media/images/')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Brands.brand')),
            ],
        ),
    ]
