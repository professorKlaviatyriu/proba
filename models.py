from django.db import models
from django.shortcuts import reverse


# Create your models here.
# таблица юристы
class Lawyer(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    body = models.TextField(blank=True, db_index=True)  # blank поле может быть пустым
    timetables = models.ManyToManyField('Timetable', blank=True, related_name='lawyers')
    cantors = models.ManyToManyField('Cantor', blank=True, related_name='lawyers')

    # глобальный слаг
    def get_absolute_url(self):
        return reverse('lawyer_detail_url', kwargs={'slug': self.slug})

    def get_abs_url(self):
        return reverse('lawyer_upgrade_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('lawyer_delete_url', kwargs={'slug': self.slug})

    # чтобы можно было записывать через консоль
    def __str__(self):
        return '{}'.format(self.name)


# создаем класс канторы
class Cantor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    #customers = models.ManyToManyField('Klient', blank=True, related_name='cantors')

    #customers = models.ForeignKey('Lawyer', on_delete=models.CASCADE, related_name='cantorrs', null=True)

    def get_absolute_url(self):
        return reverse('cantor_detail_url', kwargs={'slug': self.slug})

    def get_abs_url(self):
        return reverse('cantor_upgrade_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('cantor_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.name)


class Klient(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True)
    cantor = models.ForeignKey('Cantor', on_delete=models.CASCADE, related_name='klients')#, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('klient_detail_url', kwargs={'slug': self.slug})

    def get_abs_url(self):
        return reverse('klient_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('klient_delete_url', kwargs={'slug': self.slug})



class Timetable(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(blank=True)

    # чтобы можно было записывать через консоль
    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('timetable_detail_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('timetable_delete_url', kwargs={'slug': self.slug})
