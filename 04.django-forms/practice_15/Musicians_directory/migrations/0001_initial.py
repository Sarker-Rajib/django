# Generated by Django 4.2.7 on 2023-12-12 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default='Mr. ', max_length=40, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=40, verbose_name='Last Name')),
                ('Email', models.EmailField(max_length=254, verbose_name='Enter Your email')),
                ('PhoneNumber', models.CharField(max_length=11, verbose_name='Phone Number')),
                ('InstrumentType', models.CharField(max_length=20, verbose_name='Instrument Type')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AlbumName', models.CharField(max_length=40, verbose_name='Album Name')),
                ('rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None, max_length=5)),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicians_directory.musician')),
            ],
        ),
    ]
