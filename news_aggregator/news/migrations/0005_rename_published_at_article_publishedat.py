# Generated by Django 5.1.1 on 2024-10-05 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_image_url_article_urltoimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published_at',
            new_name='publishedAt',
        ),
    ]
