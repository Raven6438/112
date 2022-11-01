import django_filters
from . import models


class ApplicantFilter(django_filters.FilterSet):
    model = models.Applicant
    fields = ['surname', 'phone', 'birthday']