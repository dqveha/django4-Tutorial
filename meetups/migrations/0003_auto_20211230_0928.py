# Generated by Django 2.0.7 on 2021-12-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_meetup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
