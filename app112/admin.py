from django.contrib import admin

from app112 import models


@admin.register(models.EmergencyService)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'service_code', 'phone')
    list_filter = ('title', 'service_code')
    search_fields = ('title', 'service_code', 'phone')


@admin.register(models.Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic', 'birthday', 'gender', 'photo', 'phone', 'descr_state_health')
    list_filter = ('gender',)
    search_fields = ('surname', 'name', 'phone')


class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'applicant', 'date', 'status', 'number')
    list_filter = ('status',)
    search_fields = ('date', 'number')
    ordering = ('date',)


# Inline посмотреть

admin.site.register(models.Appeal, AppealAdmin)
