from django.db import models
from django.utils.translation import gettext_lazy as _
from .employee import Employee


class FavoriteEmployee(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="favorites",
        verbose_name=_("Сотрудник, на которого показывается"),
    )
    subscriber = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="subscribers",
        verbose_name=_("Подписчик, который подписывается"),
    )

    def __str__(self) -> str:
        return f'{self.subscriber} подписался на {self.employee}'
