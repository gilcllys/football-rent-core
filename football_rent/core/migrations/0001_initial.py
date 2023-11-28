# Generated by Django 4.2.6 on 2023-11-28 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FootballField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_column='name', max_length=128)),
                ('description', models.CharField(blank=True, db_column='description', max_length=144, null=True)),
            ],
            options={
                'verbose_name': 'Football field',
                'verbose_name_plural': 'Football field',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField(db_column='date_time_dt')),
                ('payment', models.BooleanField(db_column='payment', default=False)),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='FootballFieldImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(db_column='image', upload_to='')),
                ('footfield', models.ForeignKey(db_column='football_field_id', on_delete=django.db.models.deletion.CASCADE, to='core.footballfield')),
            ],
            options={
                'verbose_name': 'Football field Image',
                'verbose_name_plural': 'Football field Image',
            },
        ),
    ]
