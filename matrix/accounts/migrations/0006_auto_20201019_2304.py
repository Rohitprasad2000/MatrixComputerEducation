# Generated by Django 3.0.8 on 2020-10-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201019_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
