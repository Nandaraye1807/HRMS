from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin

from hr_allowance import models
from hr_allowance import forms
from django.db.models import Q

class AllowanceListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = models.AllowanceModel
    context_object_name = 'allowance_list'
    template_name = 'allowance_list.html'

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

class AllowanceCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("allowance_list")
    model = models.AllowanceModel
    form_class = forms.AllowanceCreateForm
    template_name = 'allowance_create.html'

class AllowanceDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("allowance_list")
    model = models.AllowanceModel
    context_object_name = "allowance"
    template_name = 'allowance_delete.html'

class AllowanceDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = models.AllowanceModel
    context_object_name = "allowance"
    template_name = 'allowance_detail.html'

class AllowanceUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy("allowance_list")
    model = models.AllowanceModel
    form_class = forms.AllowanceUpdateForm
    context_object_name = "allowance"
    template_name = 'allowance_update.html'