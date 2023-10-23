from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from hr_salary import models
from hr_salary import forms
from django.db.models import Q

class SalaryListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.SalaryModel
    context_object_name = 'salary_list'
    template_name = 'salary_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        sq = self.request.GET.get("search_query")
        search_type = self.request.GET.get("search_type")

        if sq is not None:
            if search_type == "name":
                qs = qs.filter(Q(name__icontains=sq))
            elif search_type == "salary":
                qs = qs.filter(Q(street__icontains=sq))

        return qs

class SalaryCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("salary_list")
    model = models.SalaryModel
    form_class = forms.SalaryCreateForm
    template_name = 'salary_create.html'

class SalaryDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("salary_list")
    model = models.SalaryModel
    context_object_name = "salary"
    template_name = 'salary_delete.html'

class SalaryDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.SalaryModel
    context_object_name = "salary"
    template_name = 'salary_detail.html'

class SalaryUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("salary_list")
    model = models.SalaryModel
    form_class = forms.SalaryUpdateForm
    context_object_name = "salary"
    template_name = 'salary_update.html'