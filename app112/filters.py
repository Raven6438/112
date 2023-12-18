import django_filters

from django.db.models import Q, QuerySet
from . import models, consts


class ApplicantFilter(django_filters.FilterSet):
    fullname = django_filters.CharFilter(label='ФИО', method='fullname_search')
    phone = django_filters.NumberFilter()
    birthday = django_filters.DateFilter()

    class Meta:
        model = models.Applicant
        fields = ('fullname', 'phone', 'birthday')

    def fullname_search(self, queryset, field: str, value) -> QuerySet:
        fio_list = value.split()
        match len(fio_list):
            case 1:
                surname = Q(surname__contains=value)
                name = Q(name__contains=value)
                patronymic = Q(patronymic__contains=value)

                return queryset.filter(surname | name | patronymic)
            case 2:
                surname = Q(surname__in=fio_list)
                name = Q(name__in=fio_list)
                patronymic = Q(patronymic__in=fio_list)

                return queryset.filter(surname & name | name & patronymic | surname & patronymic)
            case 3:
                surname = Q(surname__contains=fio_list[0])
                name = Q(name__contains=fio_list[1])
                patronymic = Q(patronymic__contains=fio_list[2])

                return queryset.filter(surname & name & patronymic)
            case _:
                return queryset.none()


class AppealFilter(django_filters.FilterSet):
    # fullname = django_filters.CharFilter(label='ФИО', method='fullname_search')
    service = django_filters.CharFilter(label='Код службы', field_name='service')
    status = django_filters.ChoiceFilter(label='Статус', field_name='status', choices=consts.STATUS_CHOICE)

    class Meta:
        model = models.Appeal
        fields = ('service', 'status')

    # def fullname_search(self, queryset, field: str, value) -> QuerySet:
    #     fio_list = value.split()
    #     if len(fio_list) == 1:
    #         return queryset.filter(
    #             Q(surname__contains=value) | Q(name__contains=value) | Q(patronymic__contains=value)
    #         )
    #     elif len(fio_list) == 2:
    #         surname, name, patronymic = Q(surname__in=fio_list), Q(name__in=fio_list), Q(patronymic__in=fio_list)
    #         return queryset.filter(
    #             surname & name | name & patronymic | surname & patronymic
    #         )
    #     elif len(fio_list) == 3:
    #         surname, name, patronymic = fio_list[0], fio_list[1], fio_list[2]
    #         return queryset.filter(
    #             Q(surname__contains=surname) & Q(name__contains=name) & Q(patronymic__contains=patronymic)
    #         )
    #     else:
    #         return queryset.none()
