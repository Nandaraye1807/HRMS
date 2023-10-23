from django.urls import path

from hr_allowance import views

urlpatterns = [
	path('show_allowance/', views.AllowanceListView.as_view(), name='allowance_list'),
    path('new_allowance/', views.AllowanceCreateView.as_view(), name='allowance_create'),
    path('<int:pk>', views.AllowanceDetailView.as_view(), name='allowance_detail'),
    path('<int:pk>/delete/', views.AllowanceDeleteView.as_view(), name='allowance_delete'),
    path('<int:pk>/edit/', views.AllowanceUpdateView.as_view(), name='allowance_update'),
]