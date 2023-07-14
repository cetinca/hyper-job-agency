from django import forms

from vacancy.models import Vacancy


class VacancyForm(forms.ModelForm):
    template_name = 'vacancy/vacancy_form.html'
    class Meta:
        model = Vacancy
        fields = ['description']
        exclude = ['author']
