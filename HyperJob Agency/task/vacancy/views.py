from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView

from vacancy.forms import VacancyForm
from vacancy.models import Vacancy


# Create your views here.

def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class VacancyCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = 'login'

    def get(self, request):
        form = VacancyForm()
        return render(request, 'vacancy/vacancy_create.html', {'form': form})

    def post(self, request):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.author = request.user  # Set the author as the current user
            vacancy.save()
            return redirect('vacancies')  # Redirect to vacancy detail page
        return render(request, 'vacancy/vacancy_create.html', {'form': form})

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        # Customize the behavior when the user doesn't have permission
        # For example, redirect them to a different page or show an error message
        return HttpResponseForbidden("You do not have permission to access this page.")


# Create your views here.
class VacancyListView(ListView):
    model = Vacancy
    context_object_name = 'vacancy_list'
    queryset = Vacancy.objects.all()
    template_name = 'vacancy/vacancy_list.html'
