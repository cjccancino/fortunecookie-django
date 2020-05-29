# Generated by Django 2.1.5 on 2020-05-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FortuneCookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('fortune', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['fortune'],
            },
        ),
    ]
