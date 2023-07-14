from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic.list import ListView, View

from resume.forms import ResumeForm
from resume.models import Resume


class ResumeCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login/'

    def get(self, request):
        form = ResumeForm()
        return render(request, 'vacancy/vacancy_create.html', {'form': form})

    def post(self, request):
        form = ResumeForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.author = request.user  # Set the author as the current user
            vacancy.save()
            return redirect('resumes')  # Redirect to vacancy detail page
        return render(request, 'resume/resume_create.html', {'form': form})

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        # Customize the behavior when the user doesn't have permission
        # For example, redirect them to a different page or show an error message
        return HttpResponseForbidden("You do not have permission to access this page.")


# Create your views here.
class ResumeListView(ListView):
    model = Resume
    context_object_name = 'resume_list'
    queryset = Resume.objects.all()
    template_name = 'resume/resume_list.html'
