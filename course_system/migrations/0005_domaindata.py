# Generated by Django 3.1.5 on 2022-01-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_system', '0004_domainname'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=100)),
            ],
        ),
    ]