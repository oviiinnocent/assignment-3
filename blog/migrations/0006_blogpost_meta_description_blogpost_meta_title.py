# Generated by Django 4.1.7 on 2023-03-27 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
