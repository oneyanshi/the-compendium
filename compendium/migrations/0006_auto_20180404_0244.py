# Generated by Django 2.0.3 on 2018-04-04 02:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compendium', '0005_auto_20180404_0243'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompendiumIndex',
            new_name='CompendiumIndexPage',
        ),
    ]
