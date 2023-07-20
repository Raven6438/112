from django.urls import path, register_converter, reverse_lazy
from django.views.generic import RedirectView

from . import classviews
from .classviews import Appeals, CreateApplicant, EditApplicant
from .views import *


class IDConverter:
    regex = '[0-9]\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(IDConverter, 'id')

app_name = 'app112'
urlpatterns = [
    # Отображение всех записей
    path('', RedirectView.as_view(url='/appeals/'), name='home'),
    path('applicants/', classviews.Applicants.as_view(), name='applicants'),
    path('appeals/', Appeals.as_view(), name='appeals'),
    # Создание записей
    path('applicant/create/', CreateApplicant.as_view(), name='create_applicant'),
    path('appeal/create/', create_appeal, name='create_appeal'),
    path('service/create/', create_service, name='create_service'),
    # Редактирование записей
    path('applicant/update/<int:pk>/', EditApplicant.as_view(), name='edit_applicant'),
    path('appeal/update/<int:pk>/', edit_appeal, name='edit_appeal'),
    path('service/update/<int:pk>/', edit_service, name='edit_service'),
    # Отображение записей по ID
    path('applicant/<int:pk>/', get_applicant, name='get_applicant'),
    path('service/<int:pk>/', get_service, name='get_service'),
    # Отображение других данных
    path('applicant_by_phone/', get_applicant_by_phone, name='get_applicant_by_phone'),
    path('data_json/<int:pk>/', data_json, name='data_json'),
    path('redirect/', redir, name='redirect'),
    path('redirect2/', redir2, name='redirect2')
]
