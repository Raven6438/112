from django.views.generic import ListView, CreateView, UpdateView
from django_filters.views import FilterView

from app112 import models
from app112.filters import AppealFilter
from app112.forms import FormApplicant


class Appeals(FilterView, ListView):
    model = models.Appeal
    template_name = 'app112/appeals.html'
    extra_context = {'title': 'Обращения'}
    filterset_class = AppealFilter

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class CreateApplicant(CreateView):
    form_class = FormApplicant
    template_name = 'app112/create_applicant.html'
    extra_context = {'title': 'Создание заявителя'}


class EditApplicant(UpdateView):
    model = models.Applicant
    form_class = FormApplicant
    template_name = 'app112/edit_applicant.html'
    context_object_name = 'applicant'
    extra_context = {'title': 'Редактирование заявителя'}
