# Generated by Django 4.2.4 on 2023-08-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('p_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='P_ID')),
                ('p_title', models.CharField(max_length=255)),
                ('p_short', models.CharField(max_length=255)),
                ('p_description', models.TextField()),
                ('p_img', models.FileField(default=None, max_length=255, null=True, upload_to='projects/')),
            ],
        ),
    ]
