from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['name', 'slug', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # def save(self, commit=True):

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "create":
            raise ValidationError('Slug cant be called that')

        if Timetable.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Дико извиняемся, но название "{}" занято'.format(new_slug))
        return new_slug


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = ['name', 'slug', 'body', 'timetables', 'cantors']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'timetables': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'cantors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "create":
            raise ValidationError('Slug cant be called that')

        if Lawyer.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Дико извиняемся, но название "{}" занято'.format(new_slug))
        return new_slug


class CantorForm(forms.ModelForm):
    class Meta:
        model = Cantor
        fields = ['name', 'slug', 'body']#, 'customers']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
          #  'customers': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "create":
            raise ValidationError('Slug cant be called that')

        if Cantor.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Дико извиняемся, но название "{}" занято'.format(new_slug))
        return new_slug


class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = ['name', 'slug', 'body', 'cantor']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'cantor': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "create":
            raise ValidationError('Slug cant be called that')

        if Cantor.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Дико извиняемся, но название "{}" занято'.format(new_slug))
        return new_slug
