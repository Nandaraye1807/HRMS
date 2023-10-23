from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
# Create your views here.
from hr_contacts import models
from hr_contacts import forms
from django.db.models import Q

class ContactListView(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = models.ContactModel
	context_object_name = 'contacts_list'
	template_name = 'contact_list.html'

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

class ContactCreateView(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contact_list")
	model = models.ContactModel
	form_class = forms.ContactCreateForm
	template_name = 'contact_create.html'

class ContactDeleteView(SuperuserRequiredMixin, LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contact_list")
	model = models.ContactModel
	context_object_name = "contact"
	template_name = 'contact_delete.html'

class ContactDetailView(LoginRequiredMixin, DetailView):
	login_url = reverse_lazy('login')
	model = models.ContactModel
	context_object_name = "contact"
	template_name = 'contact_detail.html'

class ContactUpdateView(SuperuserRequiredMixin, LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contact_list")
	model = models.ContactModel
	form_class = forms.ContactUpdateForm
	context_object_name = "contact"
	template_name = 'contact_update.html'


