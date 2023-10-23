from django.urls import path
from hr_employees import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('show_employee/', views.EmployeeListView.as_view(), name='employee_list'),
	path('new_employee/', views.EmployeeCreateView.as_view(), name='employee_create'),
	path('<int:pk>', views.EmployeeDetailView.as_view(), name='employee_detail'),
	path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
	path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
]