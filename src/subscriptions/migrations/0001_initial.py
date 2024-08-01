# Generated by Django 5.0.7 on 2024-07-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'permissions': (('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm')),
            },
        ),
    ]
