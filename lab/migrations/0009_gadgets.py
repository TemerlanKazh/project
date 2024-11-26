# Generated by Django 4.2.1 on 2024-02-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_subscriptions_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='gadgets',
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
                'indexes': [models.Index(fields=['-title'], name='lab_gadgets_title_51202f_idx')],
            },
        ),
    ]
