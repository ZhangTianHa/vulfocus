# Generated by Django 2.2.10 on 2020-05-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageinfo',
            name='is_share',
            field=models.BooleanField(default=False, verbose_name='镜像是否贡献'),
        ),
    ]