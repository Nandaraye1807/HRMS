from django.urls import path

from hr_salary import views

urlpatterns = [
	path('show_salary/', views.SalaryListView.as_view(), name='salary_list'),
    path('new_salary/', views.SalaryCreateView.as_view(), name='salary_create'),
    path('<int:pk>', views.SalaryDetailView.as_view(), name='salary_detail'),
    path('<int:pk>/delete/', views.SalaryDeleteView.as_view(), name='salary_delete'),
    path('<int:pk>/edit/', views.SalaryUpdateView.as_view(), name='salary_update'),
]