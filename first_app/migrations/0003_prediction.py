# Generated by Django 3.0.3 on 2020-09-09 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20200906_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('business_id', models.CharField(blank=True, max_length=100, null=True)),
                ('mark', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Prediction',
                'managed': False,
            },
        ),
    ]
