# Generated by Django 3.1.4 on 2020-12-26 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0002_auto_20201225_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_workshop', models.CharField(max_length=100)),
                ('Organized_by', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('IT', 'IT'), ('MECHANICAL', 'MECHANICAL'), ('EEE', 'EEE')], max_length=150)),
                ('Any_queeries', models.EmailField(default=False, max_length=254)),
                ('Date_of_published', models.DateTimeField(auto_now_add=True, null=True)),
                ('Date_of_conduction', models.DateTimeField()),
                ('Information', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterWorkshopUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]