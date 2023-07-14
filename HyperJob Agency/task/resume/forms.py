from django import forms

from resume.models import Resume


class ResumeForm(forms.ModelForm):
    template_name = 'resume/resume_form.html'
    class Meta:
        model = Resume
        fields = ['description']
        exclude = ['author']
