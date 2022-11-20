import django_filters
from django.db.models import Q, QuerySet
from . import models


class ApplicantFilter(django_filters.FilterSet):
    # Реализовать поиск заявителя по ФИО (в одной строке)
    fullname = django_filters.CharFilter(label='ФИО', method='fullname_search')
    phone = django_filters.NumberFilter()
    birthday = django_filters.DateFilter()

    def fullname_search(self, queryset, field: str, value) -> QuerySet:
        fio_list = value.split()

        if len(fio_list) == 1:
            return queryset.filter(
                Q(surname__contains=value) | Q(name__contains=value) | Q(patronymic__contains=value)
            )
        elif len(fio_list) == 2:
            surname, name, patronymic = Q(surname__in=fio_list), Q(name__in=fio_list), Q(patronymic__in=fio_list)
            return queryset.filter(surname & name | name & patronymic | surname & patronymic)
        elif len(fio_list) == 3:
            surname, name, patronymic = fio_list[0], fio_list[1], fio_list[2]
            return queryset.filter(
                Q(surname__contains=surname) & Q(name__contains=name) & Q(patronymic__contains=patronymic)
            )
        else:
            return queryset.none()

    class Meta:
        model = models.Applicant
        fields = ('fullname', 'phone', 'birthday')


class AppealFilter(django_filters.FilterSet):
    surname = django_filters.CharFilter(label='Фамилия', field_name='applicant__surname', lookup_expr='icontains')
    name = django_filters.CharFilter(label='Имя', field_name='applicant__name', lookup_expr='icontains')
    patronymic = django_filters.CharFilter(label='Отчество', field_name='applicant__patronymic',
                                           lookup_expr='icontains')
    service = django_filters.CharFilter(label='Код службы', field_name='service')

    class Meta:
        model = models.Appeal
        fields = ('service', 'status')
