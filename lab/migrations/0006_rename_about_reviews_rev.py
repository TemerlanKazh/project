# Generated by Django 4.2.1 on 2023-11-22 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0005_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='about',
            new_name='rev',
        ),
    ]
