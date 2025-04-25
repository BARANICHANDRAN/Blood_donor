from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonorForm
from .models import Donor
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('donor_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def donor_list(request):
    donors = Donor.objects.all()

    blood_group = request.GET.get('blood_group')
    city = request.GET.get('city')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)
    if city:
        donors = donors.filter(city=city)

    blood_groups = Donor.objects.values('blood_group').distinct()
    cities = Donor.objects.values('city').distinct()

    context = {
        'donors': donors,
        'blood_groups': blood_groups,
        'cities': cities,
    }
    return render(request, 'donor_list.html', context)

def index(request):
    return render(request, 'index.html')

def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_donor')
    else:
        form = DonorForm()
    return render(request, 'add_donor.html', {'form': form})

def view_donor(request):
    donors = Donor.objects.all()

    blood_group = request.GET.get('blood_group')
    city = request.GET.get('city')

    if blood_group:
        donors = donors.filter(blood_group=blood_group)
    if city:
        donors = donors.filter(city=city)

    blood_groups = Donor.objects.values('blood_group').distinct()
    cities = Donor.objects.values('city').distinct()

    context = {
        'donors': donors,
        'blood_groups': blood_groups,
        'cities': cities,
    }
    return render(request, 'view_donor.html', context)

def edit_donor(request, contact):
    donor = get_object_or_404(Donor, contact=contact)  

    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()  
            return redirect('donor_list')  
        else:
            return render(request, 'edit_donor.html', {'form': form, 'donor': donor})  
    else:
        form = DonorForm(instance=donor)  
        return render(request, 'edit_donor.html', {'form': form, 'donor': donor})
