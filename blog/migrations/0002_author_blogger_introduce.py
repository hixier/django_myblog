# Generated by Django 2.1.4 on 2018-12-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='blogger_introduce',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]