# Generated by Django 4.2.1 on 2023-11-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['-title']},
        ),
        migrations.AddField(
            model_name='cars',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='cars',
            index=models.Index(fields=['-title'], name='lab_cars_title_2c5cf7_idx'),
        ),
    ]
