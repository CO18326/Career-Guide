# Generated by Django 3.1.5 on 2022-01-05 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRegisterBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_user_map', to='course_system.coursedata')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course_map', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]