# Generated by Django 3.2.7 on 2021-09-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=50)),
                ('current_closed_price', models.CharField(max_length=100)),
                ('company_id', models.IntegerField()),
            ],
        ),
    ]
