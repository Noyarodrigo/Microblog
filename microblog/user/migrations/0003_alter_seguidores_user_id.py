# Generated by Django 3.2.7 on 2021-11-18 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_seguidores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguidores',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
