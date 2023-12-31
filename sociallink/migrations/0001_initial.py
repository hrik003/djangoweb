# Generated by Django 4.2.4 on 2023-08-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_name', models.CharField(max_length=255)),
                ('sl_url', models.CharField(max_length=255)),
                ('sl_icon', models.FileField(default=None, max_length=255, null=True, upload_to='social/')),
            ],
        ),
    ]
