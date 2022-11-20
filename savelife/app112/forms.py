from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import *


class FormApplicant(forms.ModelForm):  # CreateApplicant
    class Meta:
        model = Applicant
        fields = '__all__'
        widgets = {
            'descr_state_health': forms.Textarea(attrs={"cols":"55", "rows":"5"})
        }

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        if birthday > timezone.now():
            raise ValidationError("Дата рождения не должна быть в будущем времени!")
        return birthday

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) > 11:
            raise ValidationError("Номер телефона не должен превышать 11 цифр!")
        return phone


class FormAppeal(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['applicant'].empty_label = "Не выбран"

    class Meta:
        model = Appeal
        fields = '__all__'
        widgets = {
            'service': forms.CheckboxSelectMultiple(),
        }


class FormService(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service_code'].help_text = "(Примечание: Код должен быть в виде двух цифр)"

    class Meta:
        model = EmergencyService
        fields = '__all__'
