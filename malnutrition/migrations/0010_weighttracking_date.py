# Generated by Django 2.1.7 on 2019-02-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malnutrition', '0009_weighttracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='weighttracking',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
