from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название датчика")
    description = models.CharField(max_length=50, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name="Температура при измерении")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время измерения"
    )
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to="measurement_photos/",
        blank=True,
        null=True,
        verbose_name="Фотография помещения",
    )
