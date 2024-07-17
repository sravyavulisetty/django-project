# Generated by Django 4.2.14 on 2024-07-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emailId', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=200)),
                ('access', models.TextField(max_length=50)),
            ],
        ),
    ]