# Generated by Django 5.1.1 on 2024-10-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('image_url', models.URLField(blank=True, null=True)),
                ('published_at', models.DateTimeField()),
            ],
        ),
    ]