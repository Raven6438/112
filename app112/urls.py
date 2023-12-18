from django.urls import path
from django.views.generic import RedirectView

from app112 import classviews, views


app_name = 'app112'
urlpatterns = [
    # Отображение всех записей
    path('', RedirectView.as_view(url='/appeals/'), name='home'),
    path('applicants/', classviews.Applicants.as_view(), name='applicants'),
    path('appeals/', classviews.Appeals.as_view(), name='appeals'),
    # Создание записей
    path('applicant/create/', classviews.CreateApplicant.as_view(), name='create_applicant'),
    path('appeal/create/', classviews.CreateAppeal.as_view(), name='create_appeal'),
    path('service/create/', classviews.CreateEmergencyService.as_view(), name='create_service'),
    # Редактирование записей
    path('applicant/update/<int:pk>/', classviews.UpdateApplicant.as_view(), name='edit_applicant'),
    path('appeal/update/<int:pk>/', classviews.UpdateAppeal.as_view(), name='edit_appeal'),
    path('service/update/<int:pk>/', views.edit_service, name='edit_service'),
    # Отображение записей по ID
    path('applicant/<int:pk>/', classviews.Applicant.as_view(), name='get_applicant'),
    path('service/<int:pk>/', classviews.EmergencyService.as_view(), name='get_service'),
    # Отображение других данных
    path('applicant_by_phone/', views.get_applicant_by_phone, name='get_applicant_by_phone'),
    path('data_json/<int:pk>/', views.data_json, name='data_json'),
    path('redirect/', views.redir, name='redirect'),
    path('redirect2/', views.redir2, name='redirect2')
]
