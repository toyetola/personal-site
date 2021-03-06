# Generated by Django 3.1.6 on 2021-02-05 05:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('link', models.TextField(null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
