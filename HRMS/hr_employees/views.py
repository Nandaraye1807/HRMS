from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from six import text_type

from hr_employees import models
from hr_employees import forms
from django.db.models import Q

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
	logout(request)
	return redirect('login')

class EmployeeListView(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	context_object_name = 'employees_list'
	template_name = 'employee_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "name":
				qs = qs.filter(Q(name__icontains=sq))
			elif search_type == "street":
				qs = qs.filter(Q(street__icontains=sq))

		return qs


class EmployeeCreateView(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeCreateForm
	template_name = 'employee_create.html'

class EmployeeDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_delete.html'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_detail.html'

class EmployeeUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeUpdateForm
	context_object_name = "employee"
	template_name = 'employee_update.html'





