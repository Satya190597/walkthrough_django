# Generated by Django 2.0.7 on 2018-07-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_questionbank'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='category',
            field=models.CharField(default='JAVA', max_length=200),
        ),
    ]
