# Generated by Django 2.0.3 on 2018-04-04 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0008_capstonepage_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capstonepage',
            name='semester',
            field=models.CharField(max_length=250),
        ),
    ]