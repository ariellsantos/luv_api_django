# Generated by Django 3.0.7 on 2020-07-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
                ('discount_value', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
