# Generated by Django 4.2.1 on 2024-02-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_rename_reviews_review_alter_review_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('about', models.TextField(blank=True)),
                ('image', models.CharField(blank=True, default=' ', max_length=255)),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'ordering': ['-title'],
                'indexes': [models.Index(fields=['-title'], name='lab_subscri_title_836720_idx')],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('about', models.TextField(blank=True)),
                ('image', models.CharField(blank=True, default=' ', max_length=255)),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
                'ordering': ['-title'],
                'indexes': [models.Index(fields=['-title'], name='lab_game_title_30a175_idx')],
            },
        ),
    ]
