# Generated by Django 4.0.2 on 2022-03-03 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vibackend', '0005_remove_camara_strecam_delete_stream'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('idDia', models.AutoField(primary_key=True, serialize=False)),
                ('Dia', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='horario',
            name='dia',
        ),
        migrations.AddField(
            model_name='horario',
            name='idUsuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='diaHorario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vibackend.dia'),
            preserve_default=False,
        ),
    ]
