# Generated by Django 4.1.3 on 2022-11-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_image_articles_imageblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='imageBlog',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
