# Generated by Django 2.0.2 on 2022-02-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
