# Generated by Django 2.1.1 on 2018-09-15 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='gene',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='bio.Gene'),
        ),
    ]
