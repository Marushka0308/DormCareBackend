# Generated by Django 4.1.3 on 2023-10-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DormCare', '0002_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
    ]
