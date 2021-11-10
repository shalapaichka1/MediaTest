from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=70, verbose_name='Магазин')
    house_number = models.PositiveSmallIntegerField(verbose_name='Дом')
    openTime = models.TimeField(verbose_name='Время открытия',max_length=10)
    closeTime = models.TimeField(verbose_name='Время закрытия',max_length=10)
    street = models.ForeignKey("Street", on_delete=models.PROTECT, null=True, verbose_name="Магазины", related_name='shops', blank=True)


    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name']


class Street(models.Model):
    street_name = models.CharField(max_length=70, verbose_name='Улица')
    city= models.ForeignKey("City", on_delete=models.PROTECT, null=True, verbose_name="Город", related_name='streets')

    def str(self):
        return self.street_name

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"
        ordering = ['street_name']


class City(models.Model):
    city_name = models.CharField(max_length=50, verbose_name='Город')

    def str(self):
        return self.city_name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ['city_name']