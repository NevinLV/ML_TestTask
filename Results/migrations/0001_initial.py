# Generated by Django 4.0.3 on 2022-03-08 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreateQuestion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right', models.IntegerField(verbose_name='right')),
                ('wrong', models.IntegerField(verbose_name='wrong')),
                ('them', models.ForeignKey(db_column='Them_id', on_delete=django.db.models.deletion.CASCADE, to='CreateQuestion.them')),
                ('user', models.ForeignKey(db_column='User_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Result',
            },
        ),
    ]