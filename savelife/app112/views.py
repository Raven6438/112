from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView

from .forms import *
from app112 import models

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404


# создать папку view с view.py и classview.py (Пакет питона)

def for_base_temp(request):
    return render(request, 'app112/base.html', {'title': 'Главная страница'})


class Appeals(ListView):
    model = models.Appeal
    template_name = 'app112/appeals.html'
    context_object_name = 'data_appeals'
    extra_context = {'title': 'Обращения'}


"""def appeals(request):
    data_appeals = appeal.objects.all()
    return render(request, 'app112/appeals.html', {'data_appeals': data_appeals, 'title': 'Обращения', 'date': datetime.utcnow()})
"""


# Данные о заявителе с определ ID
def get_applicant(request, pk):
    applicant = get_object_or_404(Applicant, id=pk)
    return render(request, 'app112/applicant.html', {'applicant': applicant, 'title': 'Заявитель'})


def get_applicants(request):
    applicants = Applicant.objects.order_by('id').all()
    context = {
        'applicants': applicants,
        'title': 'Все заявители'
    }
    return render(request, 'app112/applicants.html', context=context)


class CreateApplicant(CreateView):
    form_class = FormApplicant
    template_name = 'app112/create_applicant.html'
    extra_context = {'title': 'Создание заявителя'}


"""
def create_applicant(request):
    form = FormApplicant(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app112:applicants')

    context = {
        'title': 'Добавить заявителя',
        'form': form
    }
    return render(request, 'app112/create_applicant.html', context=context)
"""


def create_appeal(request):  # create_appeal
    form = FormAppeal(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app112:appeals')

    context = {
        'title': 'Добавить обращение',
        'form': form
    }
    return render(request, 'app112/create_appeal.html', context=context)


def create_service(request):
    form = FormService(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app112:home')

    context = {
        'title': 'Добавить службу',
        'form': form
    }
    return render(request, 'app112/create_service.html', context=context)


class EditApplicant(UpdateView):
    model = Applicant
    form_class = FormApplicant
    template_name = 'app112/edit_applicant.html'
    context_object_name = 'applicant'
    extra_context = {'title': 'Редактирование заявителя'}


"""
def edit_applicant(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)
    if request.method == 'POST':
        form = FormApplicant(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('app112:get_applicant', pk=pk)
    else:
        form = FormApplicant(instance=applicant)

    context = {
        'title': 'Редактирование заявителя',
        'form': form,
        'pk': pk
    }
    return render(request, 'app112/edit_applicant.html', context=context)
"""


def edit_appeal(request, pk):
    appeal = get_object_or_404(Appeal, pk=pk)
    if request.method == 'POST':
        form = FormAppeal(request.POST, instance=appeal)
        if form.is_valid():
            form.save()
            return redirect('app112:get_appeal', pk=pk)
    else:
        form = FormAppeal(instance=appeal)

    context = {
        'title': 'Редактирование обращения',
        'form': form,
        'pk': pk
    }
    return render(request, 'app112/edit_appeal.html', context=context)


def edit_service(request, pk):
    pass


def redir(request):
    return redirect('app112:redirect2')


def redir2(request):
    return HttpResponse('<h1>Перенаправление с /redirect/ на /redirect2/</h1>')


def get_service(request, pk):
    serv = get_object_or_404(EmergencyService, id=pk)
    return HttpResponse(serv.title)


def get_applicant_by_phone(request):
    data = request.GET.get('phone')
    data_apl = get_object_or_404(Applicant, phone=data)
    return HttpResponse(data_apl)


def data_json(request, pk):
    applicant = get_object_or_404(Applicant, id=pk)
    result = model_to_dict(applicant)
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h>')
