# Generated by Django 4.0.5 on 2022-06-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bom',
            name='materials',
            field=models.ManyToManyField(blank=True, to='bom.bommaterial'),
        ),
    ]
