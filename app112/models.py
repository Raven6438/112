from django.db import models
import uuid
from . import consts

from django.urls import reverse


class EmergencyService(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    service_code = models.CharField(max_length=255, verbose_name='Код службы', blank=True)
    phone = models.PositiveBigIntegerField(verbose_name='Телефон', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_service', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'


class Applicant(models.Model):
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    patronymic = models.CharField('Отчество', max_length=255, blank=True)
    birthday = models.DateTimeField('День рождения', blank=True)
    gender = models.CharField('Пол', max_length=255, choices=consts.GENDER_CHOICE, default=consts.GENDER_CHOICE[0])
    photo = models.ImageField('Фотография', upload_to='photo/', default='/', blank=True)
    phone = models.PositiveBigIntegerField('Телефон', blank=True, null=True)
    descr_state_health = models.TextField('Описание состояния здоровья', blank=True, default='Практически здоров',
                                          help_text='Аллергоанамнез, хранические заболевания и т.д.')

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('app112:get_applicant', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('surname', 'name', 'patronymic')


class Appeal(models.Model):
    date = models.DateTimeField('Дата обращения', auto_now_add=True)
    number = models.UUIDField('Номер обращения', default=uuid.uuid4, unique=True, editable=False)
    incidents = models.CharField('Тип происшествия', max_length=255, choices=consts.INCIDENT_CHOICES,
                                 default=consts.INCIDENT_OTHER)
    status = models.CharField('Статус', max_length=255, choices=consts.STATUS_CHOICE, default='in work')

    count_injured = models.PositiveSmallIntegerField('Количество пострадавших', null=True, blank=True)
    dontCall = models.BooleanField('Не звонить', default=True)

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE,
                                  related_name='appeals', verbose_name='Заявитель')
    service = models.ManyToManyField(EmergencyService, related_name='appeals',
                                     verbose_name='Сервис', blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('date', 'number')
