# Generated by Django 2.0.6 on 2018-06-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180622_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='id1',
            new_name='id2',
        ),
    ]