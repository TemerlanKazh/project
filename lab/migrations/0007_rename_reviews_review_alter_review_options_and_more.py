# Generated by Django 4.2.1 on 2023-11-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_rename_about_reviews_rev'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reviews',
            new_name='Review',
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-id']},
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['-id'], name='lab_review_id_21a419_idx'),
        ),
    ]
