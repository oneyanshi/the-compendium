# Generated by Django 2.0.3 on 2018-04-12 04:07

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0011_capstonepagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='capstonepage',
            name='summary',
            field=wagtail.core.fields.RichTextField(blank=True, max_length=250),
        ),
    ]
