# Generated by Django 4.0.2 on 2022-03-09 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vibackend', '0009_camtelhorario_remove_camtel_idskedul_delete_skedul_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camtel',
            name='idUsuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
