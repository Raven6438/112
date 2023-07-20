from django.views import generic
from django_filters.views import FilterView

from app112 import models, filters
from app112.filters import AppealFilter
from app112.forms import FormApplicant


class Appeals(FilterView, generic.ListView):
    model = models.Appeal
    template_name = 'app112/appeals.html'
    extra_context = {'title': 'Обращения'}
    filterset_class = AppealFilter

    def get_queryset(self):
        return self.model.objects.order_by('-date')


class Applicants(generic.ListView):
    template_name = 'app112/applicants.html'
    context_object_name = 'applicants'

    def get_queryset(self):
        return self.get_filters().qs.order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['filter'] = self.get_filters()
        context['applicant_count'] = self.get_queryset().count()
        return context

    def get_filters(self) -> filters:
        return filters.ApplicantFilter(self.request.GET)


class CreateApplicant(generic.CreateView):
    form_class = FormApplicant
    template_name = 'app112/create_applicant.html'
    extra_context = {'title': 'Создание заявителя'}


class EditApplicant(generic.UpdateView):
    model = models.Applicant
    form_class = FormApplicant
    template_name = 'app112/edit_applicant.html'
    context_object_name = 'applicant'
    extra_context = {'title': 'Редактирование заявителя'}
