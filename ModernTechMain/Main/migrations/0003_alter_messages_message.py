# Generated by Django 4.0.5 on 2022-06-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_rename_articles_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=255, verbose_name='Текст сообщения'),
        ),
    ]