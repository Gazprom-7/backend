# Проект "Gazprom-7"

Проект представляет собой MVP web-приложения для построения организационных диаграмм, представленное командой №7 в рамках Хакатон+ по задаче от Газпром Оператор ИД.

# Стек технологий

- Python
- Django
- JWT Token

# Библиотеки

- django
- djangorestframework
- djangorestframework
- simplejwt
- pillow
- drf-spectacular

## Установка

Для запуска локально, перейдите в директории `/backend/`

Для запуска проекта вам потребуется установить Docker и docker-compose.

### Настройка проекта

1. Запустите docker compose:

```bash
docker-compose up -d
```

2. Примените миграции:

```bash
docker-compose exec backend python manage.py migrate
```

3. Создайте администратора:

```bash
docker-compose exec backend python manage.py createsuperuser
```

4. Соберите статику:

```bash
docker-compose exec backend python manage.py collectstatic
```

## Документация к API

Чтобы открыть документацию локально, запустите сервер и перейдите по ссылке:
[http://127.0.0.1/api/docs/](http://127.0.0.1/api/docs/)
