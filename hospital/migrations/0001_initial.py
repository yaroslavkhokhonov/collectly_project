# Generated by Django 2.1.7 on 2019-02-19 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_edited', models.DateTimeField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('middle_name', models.TextField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('external_id', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(editable=False)),
                ('date_edited', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('external_id', models.TextField(null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='hospital.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
