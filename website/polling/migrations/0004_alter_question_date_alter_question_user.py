# Generated by Django 4.1.5 on 2023-01-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0003_alter_question_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
