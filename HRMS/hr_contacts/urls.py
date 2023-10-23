from django.urls import path

from hr_contacts import views

urlpatterns = [
	path('show_contact/', views.ContactListView.as_view(), name='contact_list'),
	path('new_contact/', views.ContactCreateView.as_view(), name='contact_create'),
	path('<int:pk>', views.ContactDetailView.as_view(), name='contact_detail'),
	path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
	path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='contact_update'),
]