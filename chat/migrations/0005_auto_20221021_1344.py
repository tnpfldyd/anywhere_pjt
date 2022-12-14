# Generated by Django 3.2.13 on 2022-10-21 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_auto_20221021_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messageroom',
            name='fromuser',
        ),
        migrations.RemoveField(
            model_name='messageroom',
            name='touser',
        ),
        migrations.AddField(
            model_name='messageroom',
            name='from_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_user', to='accounts.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messageroom',
            name='to_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='send_user', to='accounts.user'),
            preserve_default=False,
        ),
    ]
