# Generated by Django 3.0.5 on 2020-04-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todoitem_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='date',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='addedon',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='todoitem',
            name='duedate',
            field=models.TextField(default='', max_length=100),
        ),
    ]