# Generated by Django 3.2.15 on 2022-10-23 02:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20221005_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.CharField(blank=True, editable=False, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size_l',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='size_m',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='size_s',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='size_xl',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AddField(
            model_name='product',
            name='size_xs',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
    ]