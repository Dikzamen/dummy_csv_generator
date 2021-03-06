# Generated by Django 3.2.8 on 2021-10-30 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_schemafield_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchemaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated', models.BooleanField(default=False)),
                ('rows', models.IntegerField()),
                ('schema_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dataset', to='api.schematable')),
            ],
        ),
    ]
