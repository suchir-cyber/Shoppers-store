# Generated by Django 4.2.3 on 2024-08-11 18:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0003_tag_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
