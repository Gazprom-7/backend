# Generated by Django 5.1 on 2024-08-15 14:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=31, verbose_name='Страна')),
                ('timezone', models.CharField(max_length=31, verbose_name='Часовой пояс')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=31, verbose_name='Тип образования')),
                ('university', models.CharField(max_length=127, verbose_name='Университет')),
                ('beginning', models.DateField(blank=True, null=True, verbose_name='Начало')),
                ('graduation', models.DateField(blank=True, null=True, verbose_name='Выпуск')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=31, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=31, verbose_name='Фамилия')),
                ('login', models.CharField(max_length=127, verbose_name='Логин')),
                ('password', models.CharField(max_length=127, verbose_name='Пароль')),
                ('telephone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('telephone_work', models.CharField(max_length=15, verbose_name='Рабочий телефон')),
                ('telegram', models.CharField(max_length=127, verbose_name='Телеграм')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('biography', models.TextField(blank=True, null=True, verbose_name='Биография')),
                ('technology_stack', models.CharField(max_length=127, verbose_name='Стек навыков')),
                ('start_schedule', models.TimeField(verbose_name='Начало рабочего времени')),
                ('end_schedule', models.TimeField(verbose_name='Конец рабочего времени')),
                ('dey_week', models.CharField(max_length=15, verbose_name='Рабочие дни недели')),
                ('start_absence', models.DateField(verbose_name='Начало отсутствия')),
                ('end_absence', models.DateField(verbose_name='Конец отсутствия')),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='images', verbose_name='Фото')),
                ('hobby', models.CharField(blank=True, max_length=127, null=True, verbose_name='Хобби')),
                ('interest', models.CharField(blank=True, max_length=127, null=True, verbose_name='Интересы')),
                ('success', models.CharField(blank=True, max_length=127, null=True, verbose_name='Успехи')),
                ('languages', models.CharField(max_length=127, verbose_name='Языки')),
                ('specialization', models.CharField(max_length=127, verbose_name='Специальность')),
                ('position', models.CharField(max_length=127, verbose_name='Должность')),
                ('department', models.CharField(blank=True, max_length=127, null=True, verbose_name='Отдел')),
                ('format_work', models.CharField(max_length=127, verbose_name='Формат работы')),
                ('availability', models.CharField(max_length=127, verbose_name='Доступность')),
                ('grade', models.CharField(max_length=127, verbose_name='Квалификация')),
                ('staff', models.BooleanField(default=True, verbose_name='Сотрудник отдела')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.address', verbose_name='Адрес')),
                ('deputy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deputies', to='employee.employee', verbose_name='Заместитель')),
                ('leadership', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leaders', to='employee.employee', verbose_name='Руководитель')),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.education', verbose_name='Университет')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
