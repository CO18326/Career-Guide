# Generated by Django 3.1.5 on 2022-01-05 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('organisation', models.CharField(choices=[('Profesor', 'Profesor'), ('Student', 'Student')], max_length=30)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1, null=True)),
                ('passout_year', models.IntegerField(null=True)),
                ('placement_year', models.IntegerField(null=True)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('CIVIL', 'CIVIL'), ('ECE', 'ECE'), ('MECH', 'MECH')], max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
