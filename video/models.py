from django.db import models


CATEGORY_CHOICES = (
    (1, "Фондовый рынок статус PRO"),
)


class Video(models.Model):
    head = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    body = models.TextField(
        blank=True,
        null=True,
    )

    link = models.URLField(
        max_length=200,
        blank=False,
        null=False,
    )

    category_id = models.IntegerField(
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False,
    )

    idx = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )

    date_create = models.DateTimeField(
        auto_now_add=True,
    )

    date_update = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['idx', 'pk']
        db_table = 'kase_video'

    def __str__(self):
        return self.head
