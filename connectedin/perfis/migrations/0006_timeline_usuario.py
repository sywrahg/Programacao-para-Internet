# Generated by Django 2.0 on 2018-02-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfis', '0005_auto_20180223_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_timeline', to=settings.AUTH_USER_MODEL),
        ),
    ]
