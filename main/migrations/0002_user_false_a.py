# Generated by Django 3.2 on 2021-10-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='false_a',
            field=models.ManyToManyField(related_name='user_false', to='main.Quizzes'),
        ),
    ]