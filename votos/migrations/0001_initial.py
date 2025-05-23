# Generated by Django 5.0.2 on 2025-03-30 14:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propuestas', '0010_remove_version_propuesta_remove_version_usuario_and_more'),
        ('versiones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Voto_Propuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('propuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votos_propuesta', to='propuestas.propuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos_propuesta', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voto_Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos_version', to=settings.AUTH_USER_MODEL)),
                ('version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votos_version', to='versiones.version')),
            ],
        ),
    ]
