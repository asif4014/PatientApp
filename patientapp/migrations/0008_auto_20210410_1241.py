# Generated by Django 3.1.7 on 2021-04-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0007_auto_20210410_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
