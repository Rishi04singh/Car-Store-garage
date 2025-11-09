from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages  # ✅ Import Django messages framework

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the data to your Contact model
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()

        # ✅ Add success message
        messages.success(request, "✅ Your message has been sent successfully! We’ll contact you soon.")
        return redirect('contact')  # Redirect to the same page so refresh doesn't resubmit form

    return render(request, 'contact.html')


def newvehicles(request):
    return render(request, 'newvehicles.html')

def repair(request):
    return render(request, 'repair.html')

def usedvehicles(request):
    return render(request, 'usedvehicles.html')
