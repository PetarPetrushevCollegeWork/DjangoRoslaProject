from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import installation, consultation


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "password1", "password2"]


class InstallationBookingForm(forms.ModelForm):
    class Meta:
        model = installation
        fields = ["installDate", "productType"]
        widgets = {
            "installDate": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["installDate"].input_formats = ["%Y-%m-%dT%H:%M"]

    def clean_installDate(self):
        install_date = self.cleaned_data["installDate"]
        if installation.objects.filter(installDate=install_date).exists() or consultation.objects.filter(consultDate=install_date).exists():
            raise forms.ValidationError("A booking already exists for this date and time.")
        return install_date


class ConsultationBookingForm(forms.ModelForm):
    class Meta:
        model = consultation
        fields = ["consultDate", "consultType"]
        widgets = {
            "consultDate": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["consultDate"].input_formats = ["%Y-%m-%dT%H:%M"]

    def clean_consultDate(self):
        consult_date = self.cleaned_data["consultDate"]
        if consultation.objects.filter(consultDate=consult_date).exists() or installation.objects.filter(installDate=consult_date).exists():
            raise forms.ValidationError("A booking already exists for this date and time.")
        return consult_date