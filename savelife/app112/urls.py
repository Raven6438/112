from django.urls import path, register_converter

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
    path('', for_base_temp, name='home'),
    path('applicants/', get_applicants, name='applicants'),
    path('appeals/', Appeals.as_view(), name='appeals'),
    # Создание записей
    path('createApplicant/', CreateApplicant.as_view(), name='create_applicant'),
    path('createAppeal/', create_appeal, name='create_appeal'),
    path('createService/', create_service, name='create_service'),
    # Редактирование записей
    path('editApplicant/<int:pk>/', EditApplicant.as_view(), name='edit_applicant'),
    path('editAppeal/<int:pk>/', edit_appeal, name='edit_appeal'),
    path('editService/<int:pk>/', edit_service, name='edit_service'),
    # Отображение записей по ID
    path('applicant/<int:pk>/', get_applicant, name='get_applicant'),
    path('service/<int:pk>/', get_service, name='get_service'),
    # Отображение других данных
    path('applicant_by_phone/', get_applicant_by_phone, name='get_applicant_by_phone'),
    path('data_json/<int:pk>/', data_json, name='data_json'),
    path('redirect/', redir, name='redirect'),
    path('redirect2/', redir2, name='redirect2')
]
