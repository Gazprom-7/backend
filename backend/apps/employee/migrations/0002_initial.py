# Generated by Django 5.1 on 2024-08-18 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='teams',
            field=models.ManyToManyField(related_name='teams_employee', to='team.team', verbose_name='Команды'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='favoriteemployee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='employee.employee', verbose_name='Сотрудник, на которого показывается'),
        ),
        migrations.AddField(
            model_name='favoriteemployee',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='employee.employee', verbose_name='Подписчик, который подписывается'),
        ),
        migrations.AddField(
            model_name='employee',
            name='interest',
            field=models.ManyToManyField(to='employee.interest', verbose_name='Интересы'),
        ),
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(to='employee.skill', verbose_name='Навыки'),
        ),
    ]
