# Generated by Django 3.1.7 on 2022-02-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientapp', '0003_auto_20220128_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='empinfo',
            name='resume_path',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='empinfo',
            name='resume',
            field=models.FileField(upload_to='Resumes/'),
        ),
    ]
