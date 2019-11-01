# Generated by Django 2.2.2 on 2019-07-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_type', models.CharField(max_length=20)),
                ('host', models.CharField(max_length=100, unique=True)),
                ('port', models.IntegerField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('options', models.TextField()),
            ],
        ),
    ]