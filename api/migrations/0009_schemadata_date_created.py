# Generated by Django 3.2.8 on 2021-10-30 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_schemadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemadata',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
