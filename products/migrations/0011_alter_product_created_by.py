# Generated by Django 3.2.15 on 2022-10-23 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0010_alter_product_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to='profiles.userprofile'),
        ),
    ]