# Generated by Django 3.0.8 on 2020-10-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_attendance_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
