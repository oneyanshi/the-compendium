# Generated by Django 2.0.3 on 2018-04-04 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0003_auto_20180403_0434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='page',
        ),
        migrations.DeleteModel(
            name='BlogPageGalleryImage',
        ),
    ]
