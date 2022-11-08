import django_filters
from django_filters.widgets import LinkWidget
from django.shortcuts import get_object_or_404
from . import models
from .models import EmergencyService, Appeal


class ApplicantFilter(django_filters.FilterSet):
    # surname = django_filters.CharFilter(field_name='surname', lookup_expr='icontains')

    class Meta:
        model = models.Applicant
        fields = ('surname', 'name', 'patronymic', 'phone', 'birthday')


class AppealFilter(django_filters.FilterSet):
    surname = django_filters.CharFilter(label='Фамилия', field_name='applicant__surname', lookup_expr='icontains')
    name = django_filters.CharFilter(label='Имя', field_name='applicant__name', lookup_expr='icontains')
    patronymic = django_filters.CharFilter(label='Отчество', field_name='applicant__patronymic',
                                           lookup_expr='icontains')
    service = django_filters.CharFilter(label='Код службы', field_name='service')

    class Meta:
        model = models.Appeal
        fields = ('service', 'status')
