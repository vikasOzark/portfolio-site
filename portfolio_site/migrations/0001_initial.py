# Generated by Django 3.2.6 on 2021-10-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=50)),
                ('person_l_name', models.CharField(max_length=50)),
                ('person_number', models.IntegerField(max_length=12)),
                ('person_email', models.EmailField(max_length=50)),
                ('person_message', models.TextField(max_length=100)),
            ],
        ),
    ]
