# Generated by Django 3.2.5 on 2021-10-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211020_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='false_a',
            field=models.ManyToManyField(related_name='user_false', to='main.Quizzes'),
        ),
        migrations.AlterField(
            model_name='user',
            name='true_a',
            field=models.ManyToManyField(related_name='user_true', to='main.Quizzes'),
        ),
    ]
