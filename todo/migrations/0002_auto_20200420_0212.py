# Generated by Django 3.0.5 on 2020-04-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date',
            field=models.TextField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='task',
            field=models.TextField(blank=True, default=None, max_length=100, null=True),
        ),
    ]