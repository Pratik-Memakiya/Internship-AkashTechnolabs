# Generated by Django 3.2.3 on 2021-06-10 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('enrollment_num', models.IntegerField()),
            ],
        ),
    ]
