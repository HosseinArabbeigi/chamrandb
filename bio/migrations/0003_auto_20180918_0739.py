# Generated by Django 2.1.1 on 2018-09-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_auto_20180915_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='gene',
            name='detail',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='gene',
            name='code',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='gene',
            name='sequence',
            field=models.URLField(),
        ),
    ]
