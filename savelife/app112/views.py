from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from . import filters
from . import forms
from . import models


def for_base_temp(request):
    return render(request, 'app112/base.html', {'title': 'Главная страница'})


def get_applicant(request, pk):
    applicant = get_object_or_404(models.Applicant, id=pk)
    return render(request, 'app112/applicant.html', {'applicant': applicant, 'title': 'Заявитель'})


def get_applicants(request):
    applicants = models.Applicant.objects.order_by('-id').all()
    filter = filters.ApplicantFilter(request.GET, queryset=applicants)
    context = {
        'title': 'Все заявители',
        'filter': filter,
        'applicant_count': len(applicants)
    }
    return render(request, 'app112/applicants.html', context=context)


def create_appeal(request):  # create_appeal
    form = forms.FormAppeal(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app112:appeals')

    context = {
        'title': 'Добавить обращение',
        'form': form
    }
    return render(request, 'app112/create_appeal.html', context=context)


def create_service(request):
    form = forms.FormService(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('app112:home')

    context = {
        'title': 'Добавить службу',
        'form': form
    }
    return render(request, 'app112/create_service.html', context=context)


def edit_appeal(request, pk):
    appeal = get_object_or_404(models.Appeal, pk=pk)
    if request.method == 'POST':
        form = forms.FormAppeal(request.POST, instance=appeal)
        if form.is_valid():
            form.save()
            return redirect('app112:appeals')
    else:
        form = forms.FormAppeal(instance=appeal)

    context = {
        'title': 'Редактирование обращения',
        'form': form,
        'pk': pk
    }
    return render(request, 'app112/edit_appeal.html', context=context)


def edit_service(request, pk):
    service = get_object_or_404(models.EmergencyService, pk=pk)
    if request.method == 'POST':
        form = forms.FormService(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('app112:get_service', pk)
    else:
        form = forms.FormService(instance=service)

    context = {
        'title': 'Редактирование службы',
        'form': form,
        'pk': pk
    }
    return render(request, 'app112/edit_service.html', context=context)


def redir(request):
    return redirect('app112:redirect2')


def redir2(request):
    return HttpResponse('<h1><a href="http://127.0.0.1:8000/redirect/">http://127.0.0.1:8000/redirect/</a> '
                        '- недоступен.<hr>Выбыли перенаправлены на: '
                        '<a href="http://127.0.0.1:8000/redirect2/">http://127.0.0.1:8000/redirect2/</a></h1>'
                        '<a href="http://127.0.0.1:8000/">Назад</a>')


def get_service(request, pk):
    service = get_object_or_404(models.EmergencyService, id=pk)
    context = {
        'service': service
    }
    return render(request, 'app112/service.html', context=context)


def get_applicant_by_phone(request):
    data = request.GET.get('phone')
    data_apl = get_object_or_404(models.Applicant, phone=data)
    return HttpResponse(data_apl)


def data_json(request, pk):
    applicant = get_object_or_404(models.Applicant, id=pk)
    result = model_to_dict(applicant)
    result['photo'] = str(result['photo'])
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h>')
