from typing import Iterable

from django.utils import timezone

from app112 import models
from app112.utils.tests.faker_init import faker_ru
import factory


class EmergencyService(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda _: faker_ru.word())
    service_code = factory.Sequence(lambda _: faker_ru.word())
    phone = factory.Sequence(lambda _: faker_ru.pyint(min_value=0))

    class Meta:
        model = models.EmergencyService


class Applicant(factory.django.DjangoModelFactory):
    surname = factory.Sequence(lambda _: faker_ru.last_name())
    name = factory.Sequence(lambda _: faker_ru.first_name())
    patronymic = factory.Sequence(lambda _: faker_ru.middle_name())
    birthday = factory.Sequence(lambda _: faker_ru.date_time(tzinfo=timezone.utc))
    phone = factory.Sequence(lambda _: faker_ru.pyint(min_value=0))

    class Meta:
        model = models.Applicant


class Appeal(factory.django.DjangoModelFactory):
    count_injured = factory.Sequence(lambda _: faker_ru.pyint(min_value=0, max_value=100))
    applicant = factory.SubFactory(Applicant)

    class Meta:
        model = models.Appeal

    @factory.post_generation
    def service(self, create: bool, extracted: Iterable[models.EmergencyService], **kwargs: dict) -> None:
        if not create:
            return
        if extracted:
            for service in extracted:
                self.service.add(service)
