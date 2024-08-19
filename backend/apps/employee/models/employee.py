from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .address import Address
from .education import Education
from .interest import Interest
from .skills import Skill

User = get_user_model()


class Employee(models.Model):
    DEPARTMENT = (
        ("Разработка", "Разработка"),
        ("Архитектура", "Архитектура"),
        ("ИБ", "ИБ"),
        ("Аналитика", "Аналитика"),
        ("Инфраструктура", "Инфраструктура"),
    )
    firstname = models.CharField(_("Имя"), max_length=31)
    lastname = models.CharField(_("Фамилия"), max_length=31)
    login = models.CharField(_("Логин"), max_length=127)
    password = models.CharField(_("Пароль"), max_length=127)
    telephone = models.CharField(_("Телефон"), max_length=15)
    telephone_work = models.CharField(_("Рабочий телефон"), max_length=15)
    default_telephone = models.BooleanField(
        _("Телефон по умолчанию"), default=True
    )
    telegram = models.CharField(_("Телеграм"), max_length=127)
    email = models.EmailField(_("Электронная почта"))
    leadership = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="leaders",
        verbose_name=_("Руководитель"),
    )
    biography = models.TextField(_("Биография"), null=True, blank=True)
    start_schedule = models.TimeField(_("Начало рабочего времени"))
    end_schedule = models.TimeField(_("Конец рабочего времени"))
    dey_week = models.CharField(_("Рабочие дни недели"), max_length=15)
    start_absence = models.DateField(
        _("Начало отсутствия"), null=True, blank=True
    )
    end_absence = models.DateField(
        _("Конец отсутствия"), null=True, blank=True
    )
    image = models.ImageField(
        _("Фото"),
        null=True,
        blank=True,
        upload_to="images",
        default="default.jpg",
    )
    hobby = models.CharField(_("Хобби"), max_length=127, null=True, blank=True)
    success = models.CharField(
        _("Успехи"), max_length=127, null=True, blank=True
    )
    education = models.ManyToManyField(
        Education,
        verbose_name=_("Университет"),
        blank=True,
    )
    languages = models.CharField(_("Языки"), max_length=127)
    deputy = models.ForeignKey(
        "self",
        verbose_name=_("Заместитель"),
        null=True,
        blank=True,
        related_name="deputies",
        on_delete=models.SET_NULL,
    )
    position = models.CharField(_("Должность"), max_length=127)
    department = models.CharField(
        _("Отдел"), max_length=127, null=True, blank=True, choices=DEPARTMENT
    )
    format_work = models.CharField(_("Формат работы"), max_length=127)
    availability = models.CharField(_("Доступность"), max_length=127)
    grade = models.CharField(_("Квалификация"), max_length=127)
    staff = models.BooleanField(_("Сотрудник отдела"), default=True)
    address = models.ForeignKey(
        Address,
        verbose_name=_("Адрес"),
        on_delete=models.SET_NULL,
        null=True,
    )
    subordinates = models.ManyToManyField(
        "self",
        verbose_name=_("Подчиненные"),
        blank=True,
        related_name="superiors",
        symmetrical=False,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
        null=True,
        blank=True,
        related_name="employee",
    )
    teams = models.ManyToManyField(
        "team.Team",
        verbose_name=_("Команды"),
        related_name="teams_employee",
        blank=True,
    )
    projects = models.ManyToManyField(
        "team.Project",
        verbose_name=_("Проекты"),
        blank=True,
        related_name="projects_employee",
    )
    skills = models.ManyToManyField(Skill, verbose_name=_("Навыки"))
    interest = models.ManyToManyField(Interest, verbose_name=_("Интересы"))

    @property
    def work_time(self):
        return f"{self.start_schedule} - {self.end_schedule}"

    @property
    def absence(self):
        return f"{self.start_absence} - {self.end_absence}"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
