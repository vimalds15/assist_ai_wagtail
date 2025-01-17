# Generated by Django 5.1.3 on 2024-11-27 06:55

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('header', 3)], blank=True, block_lookup={0: ('wagtail.images.blocks.ImageBlock', [], {}), 1: ('wagtail.blocks.URLBlock', (), {}), 2: ('wagtail.blocks.CharBlock', (), {}), 3: ('wagtail.blocks.StructBlock', [[('header_logo', 0), ('header_logo_url', 1), ('header_cta', 2)]], {})}, null=True),
        ),
    ]
