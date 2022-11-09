# Generated by Django 3.0.5 on 2020-05-03 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.Persona')),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('administracion.persona',),
        ),
    ]
