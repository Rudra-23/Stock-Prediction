# Generated by Django 3.2.7 on 2021-09-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_companies_type_of_investment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='id',
        ),
        migrations.AlterField(
            model_name='companies',
            name='company_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
