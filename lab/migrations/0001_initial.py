# Generated by Django 4.2.1 on 2023-11-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True)),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
