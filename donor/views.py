from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonorForm
from .models import Donor
from django.db import models

def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()
    return render(request, 'add_donor.html', {'form': form})

def donor_list(request):
    blood_groups = Donor.objects.values('blood_group').distinct()
    blood_group_filter = request.GET.get('blood_group', '')
    donors = Donor.objects.all()
    if blood_group_filter:
        donors = donors.filter(blood_group=blood_group_filter)
    
    return render(request, 'donor_list.html', {
        'donors': donors,
        'blood_groups': blood_groups
    })
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
