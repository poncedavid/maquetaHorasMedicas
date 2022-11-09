# Generated by Django 3.0.5 on 2020-05-03 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Cita_medica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField(blank=True, null=True)),
                ('hora_inicio_cita', models.TimeField()),
                ('hora_fin_cita', models.TimeField()),
                ('estado_cita', models.CharField(choices=[('SOL', 'Solicitada'), ('CONF', 'Confirmada'), ('ANUL', 'Anulada'), ('REA', 'Realizada')], default='SOL', max_length=20)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Paciente')),
            ],
        ),
    ]
