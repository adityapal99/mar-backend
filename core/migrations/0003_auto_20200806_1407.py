# Generated by Django 3.0 on 2020-08-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200806_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='linkToProof',
            field=models.TextField(),
        ),
    ]
