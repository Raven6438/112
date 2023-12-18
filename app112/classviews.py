from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from app112 import models, forms, filters


class Appeals(FilterView, generic.ListView):
    model = models.Appeal
    template_name = 'app112/appeals.html'
    extra_context = {'title': 'Обращения'}
    filterset_class = filters.AppealFilter

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class CreateAppeal(generic.CreateView):
    model = models.Appeal
    template_name = 'app112/create_appeal.html'
    form_class = forms.FormAppeal
    extra_context = {'title': 'Добавить обращение'}
    success_url = reverse_lazy('app112:home')


class Applicants(generic.ListView):
    template_name = 'app112/applicants.html'
    context_object_name = 'applicants'

    def get_context_data(self, *, object_list: list = None, **kwargs: dict) -> dict:
        context = super().get_context_data(object_list=None, **kwargs)
        context['filter'] = self.get_filter()
        context['applicant_count'] = self.get_queryset().count()

        return context

    def get_queryset(self) -> QuerySet[models.Applicant]:
        applicant_filter = self.get_filter()
        return applicant_filter.qs.order_by('-id')

    def get_filter(self) -> filters:
        return filters.ApplicantFilter(self.request.GET)


class Applicant(generic.DetailView):
    model = models.Applicant
    template_name = 'app112/applicant.html'
    context_object_name = 'applicant'
    extra_context = {'title': 'Заявитель'}


class CreateApplicant(generic.CreateView):
    form_class = forms.FormApplicant
    template_name = 'app112/create_applicant.html'
    extra_context = {'title': 'Создание заявителя'}


class UpdateApplicant(generic.UpdateView):
    model = models.Applicant
    form_class = forms.FormApplicant
    template_name = 'app112/edit_applicant.html'
    extra_context = {'title': 'Редактирование заявителя'}
    context_object_name = 'applicant'


class EmergencyService(generic.DetailView):
    model = models.EmergencyService
    template_name = 'app112/service.html'
    context_object_name = 'service'
    extra_context = {'title': 'Экстренная служба'}
