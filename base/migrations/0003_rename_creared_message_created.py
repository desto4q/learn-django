# Generated by Django 4.2.1 on 2023-06-02 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='creared',
            new_name='created',
        ),
    ]
