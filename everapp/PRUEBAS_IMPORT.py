

from .utils import notify_users  # Import your notification function
from .forms import PropertyForm
from django.shortcuts import render, redirect
from django.urls import reverse

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            new_property = form.save()  # Save the new property object
            property_url = request.build_absolute_uri(reverse('property_detail', args=[new_property.id]))
            notify_users(new_property, property_url)  # Notify users with property details and URL
            return redirect('home')  # Replace with your success URL
    else:
        form = PropertyForm()
    
    return render(request, 'add_property.html', {'form': form})