from django import forms
from django.contrib.auth.models import User

from .models import Business, Employee


class BusinessForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

    class Meta:
        model = Business
        fields = ('name',)


class EmployeeForm(forms.ModelForm):
    order = forms.ChoiceField(choices=[(i, x) for i, x in enumerate(Business.objects.all())])
    employee = forms.ChoiceField(choices=[(i, x) for i, x in enumerate(User.objects.all())])

    class Meta:
        model = Employee
        fields = ('employee', 'order',)
