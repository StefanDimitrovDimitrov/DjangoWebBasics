# Generated by Django 3.2 on 2021-05-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django102', '0009_auto_20210507_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
