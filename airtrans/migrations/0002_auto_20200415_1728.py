# Generated by Django 3.0.5 on 2020-04-15 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtrans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_date',
            field=models.DateField(),
        ),
    ]