# Generated by Django 3.1.2 on 2021-12-24 13:06

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
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fullname', models.CharField(max_length=200)),
                ('college_name', models.CharField(max_length=200)),
                ('current_year_of_study', models.CharField(max_length=10)),
                ('expected_year_of_passing_out', models.IntegerField()),
                ('expected_year_of_sitting_for_placement', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
