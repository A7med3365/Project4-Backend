# Generated by Django 4.2.3 on 2023-07-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_category_product_categoryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_urls',
            field=models.JSONField(blank=True, default=list, null=True, verbose_name='Image URLs'),
        ),
        migrations.AddField(
            model_name='product',
            name='poster_image_url',
            field=models.URLField(blank=True, error_messages={'required': 'poster_image_url field is required.'}, null=True, verbose_name='Poster Image URL'),
        ),
    ]