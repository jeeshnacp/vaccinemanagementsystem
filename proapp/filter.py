from django_filters import CharFilter

from django import forms
from proapp.models import hospital, nurse, customer, vaccine
import django_filters


class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='place', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Place', 'class': 'form-control'}))

    class Meta:
        model = hospital
        fields = ['name']

class NurseFilter(django_filters.FilterSet):
    name = CharFilter(field_name='Nurse_Name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = nurse
        fields = ['name']

class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='Name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = customer
        fields = ['name']

class VaccineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = vaccine
        fields = ['name']

class NVaccineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='vaccine_name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = vaccine
        fields = ['name']

class NUserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='Name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = customer
        fields = ['name']

class NHospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='place', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Place', 'class': 'form-control'}))

    class Meta:
        model = hospital
        fields = ['name']
