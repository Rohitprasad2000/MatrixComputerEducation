# Generated by Django 3.0.8 on 2020-11-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_extenduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
