# Generated by Django 4.2.4 on 2023-08-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0003_remove_webservice_id_webservice_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webservice',
            name='service_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='S_ID'),
        ),
    ]
