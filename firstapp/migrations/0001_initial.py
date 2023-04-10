# Generated by Django 3.2 on 2022-12-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
