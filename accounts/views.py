from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST

from .forms import CustomUserCreationForm, ProfileUpdateForm


def _dashboard_url_for(user):
    if user.role == 'ADMIN':
        return 'admin_dashboard'
    return 'member_dashboard'


def register_view(request):
    if request.user.is_authenticated:
        return redirect(_dashboard_url_for(request.user))
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully. Welcome!')
            return redirect(_dashboard_url_for(user))
        messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(_dashboard_url_for(request.user))
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect(_dashboard_url_for(user))
        messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@require_POST
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def dashboard_redirect(request):
    return redirect(_dashboard_url_for(request.user))


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})


@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        messages.error(request, 'You do not have access to the admin dashboard.')
        return redirect('member_dashboard')
    return render(request, 'accounts/admin_dashboard.html')


@login_required
def member_dashboard(request):
    return render(request, 'accounts/member_dashboard.html')