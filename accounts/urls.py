from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/member/', views.member_dashboard, name='member_dashboard'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url='/profile/'
    ), name='password_change'),
]