# Generated by Django 2.1.1 on 2018-09-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('waiting', 'Waiting'), ('watching', 'Watching'), ('stopped', 'Stoped')], default='waiting', max_length=16),
        ),
    ]
