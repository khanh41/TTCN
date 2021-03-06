# Generated by Django 3.1.4 on 2020-12-22 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0014_auto_20201211_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('jobpost_connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='jobs.joblisting')),
            ],
        ),
    ]
