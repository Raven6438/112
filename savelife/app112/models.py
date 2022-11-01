from django.db import models
import uuid


# Модель "Экстр Службы"
# Название класса с большой буквы
from django.urls import reverse


class EmergencyService(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')  # max_len = 255
    service_code = models.CharField(max_length=255, verbose_name='Код службы', blank=True)
    phone = models.PositiveBigIntegerField(verbose_name='Телефон',   null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_service', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'


# Модель "Заявитель"
class Applicant(models.Model):
    GENDER_CHOICE = (
        ('m', 'Мужчина'),
        ('w', 'Женщина')
    )
    surname = models.CharField('Фамилия', max_length=255)
    name = models.CharField('Имя', max_length=255)
    patronymic = models.CharField('Отчество', max_length=255, blank=True)
    birthday = models.DateTimeField('День рождения', null=True)
    gender = models.CharField('Пол', max_length=255, choices=GENDER_CHOICE, default='m')
    photo = models.ImageField('Фотография', upload_to='photo/', blank=True)
    phone = models.PositiveBigIntegerField('Телефон', blank=True, null=True)
    descr_state_health = models.TextField('Описание состояния здоровья', blank=True, default='Практически здоров',
                                          help_text='Аллергоанамнез, хранические заболевания и т.д.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app112:get_applicant', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('surname', 'name', 'patronymic')


# Модель "Обращение"
class Appeal(models.Model):
    STATUS_CHOICE = (
        ('in work', 'В работе'),
        ('completed', 'Завершено')
    )
    date = models.DateTimeField('Дата обращения', auto_now_add=True)
    number = models.UUIDField('Номер обращения', default=uuid.uuid4, unique=True, editable=False)  # без appeal
    status = models.CharField('Статус', max_length=255, choices=STATUS_CHOICE, default='in work')

    count_injured = models.PositiveSmallIntegerField('Количество пострадавших', null=True, blank=True)
    dontCall = models.BooleanField('Не звонить', default=True)

    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='appeals',
                                  verbose_name='Заявитель')
    service = models.ManyToManyField(EmergencyService, related_name='appeals',  # без id
                                     verbose_name='ID сервиса', blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('date', 'number')


"""class Incident(models.Model):
    num_inc = models.UUIDField(default=uuid.uuid4(), unique=True, editable=False, db_index=True,
                               verbose_name='Номер происшествия')
    title = models.CharField(max_length=100, verbose_name='Название')
    count_injured = models.PositiveSmallIntegerField(verbose_name='Количество пострадавших')
    dontCall = models.BooleanField(default=True, verbose_name='Не звонить')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Происшествия'
        verbose_name_plural = 'Происшествия'
        ordering = ['id']
"""
