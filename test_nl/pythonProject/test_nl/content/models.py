from django.db import models
from django.urls import reverse


from polymorphic.models import PolymorphicModel


class Page(models.Model):
    title = models.CharField("Заголовок", max_length=200, blank=True)
    is_active = models.BooleanField(
        default=False, verbose_name="Активно", db_index=True
    )

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ("id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("page:page_detail", kwargs={"pk": self.id})


class Content(PolymorphicModel):
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    title = models.CharField("Заголовок", max_length=100, blank=True, db_index=True)
    counter = models.PositiveIntegerField(
        "Счетчик просмотров", default=0, editable=False
    )
    page = models.ForeignKey(
        to="Page",
        verbose_name="Страница",
        on_delete=models.CASCADE,
        related_name="content",
    )

    class Meta(PolymorphicModel.Meta):
        verbose_name = "Блок контента"
        verbose_name_plural = "Блоки контента"
        ordering = ("order",)

    def __str__(self):
        return self.title


class Video(Content):
    video_url = models.URLField("Ссылка на файл")
    subtitle_url = models.URLField("Ссылка на субтитры")

    class Meta(PolymorphicModel.Meta):
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
        ordering = ("order",)


class Audio(Content):
    bitrate = models.PositiveIntegerField(
        "Битрейт",
    )

    class Meta(PolymorphicModel.Meta):
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"
        ordering = ("order",)


class Text(Content):
    some_text = models.TextField("Текст")

    class Meta(PolymorphicModel.Meta):
        verbose_name = "Текст"
        verbose_name_plural = "Текст"
        ordering = ("order",)
