from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonorForm
from .models import Donor
from django.db import models


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
def edit_donor(request,contact):
    if request.method == "POST":
        if "update" in request.POST:
            contact = request.POST.get("contact")
            try:
                donor = Donor.objects.get(contact=contact)
                donor.name = request.POST.get("name")
                donor.blood_group = request.POST.get("blood_group")
                donor.city = request.POST.get("city")
                donor.last_donated = request.POST.get("last_donated") or None
                donor.save()
                messages.success(request, "Donor updated successfully.")
                return redirect('edit_donor')
            except Donor.DoesNotExist:
                messages.error(request, "Donor not found.")
        else:
            contact = request.POST.get("contact")
            try:
                donor = Donor.objects.get(contact=contact)
                return render(request, 'edit_donor.html', {'donor': donor})
            except Donor.DoesNotExist:
                messages.error(request, "Donor not found.")
                return render(request, 'edit_donor.html')
    
    return render(request, 'edit_donor.html')
