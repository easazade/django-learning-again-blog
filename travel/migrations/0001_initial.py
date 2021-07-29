# Generated by Django 3.2.5 on 2021-07-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
                ('distance', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
