# Generated by Django 4.2.3 on 2023-07-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
