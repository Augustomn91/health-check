# Generated by Django 4.0.2 on 2022-02-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_check', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
