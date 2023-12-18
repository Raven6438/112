from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from app112 import models


class FormApplicant(forms.ModelForm):
    class Meta:
        model = models.Applicant
        fields = '__all__'
        widgets = {
            'descr_state_health': forms.Textarea(attrs={'cols': '55', 'rows': '5'})
        }

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')

        if birthday > timezone.now():
            raise ValidationError('Дата рождения не должна быть в будущем времени!')
        return birthday

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if len(str(phone)) > 11:
            raise ValidationError('Номер телефона не должен превышать 11 цифр!')
        if len(str(phone)) < 6:
            raise ValidationError('Номер телефона не должен быть меньше 6 цифр!')
        return phone


class FormAppeal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].empty_label = 'Не выбран'
        self.fields['incidents'].empty_label = 'Не выбран'

    class Meta:
        model = models.Appeal
        fields = '__all__'
        widgets = {
            'service': forms.CheckboxSelectMultiple(),
            'dontCall': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class FormService(forms.ModelForm):
    class Meta:
        model = models.EmergencyService
        fields = '__all__'
        help_texts = {
            'service_code': 'Примечание: Код должен быть в виде двух цифр'
        }
