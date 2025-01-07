from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.
def home(request):
    venues = Venue.objects.filter(availability=True)
    catering = Catering.objects.all()
    stagedecoration = StageDecoration.objects.all()
    photography = Photography.objects.all()
    weddingpackage = WeddingPackage.objects.all()
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_form')
    else:
        form = ContactForms()
    return render(request,'index.html', {"venues": venues , 'catering':catering , 'photography':photography , 'stagedecoration':stagedecoration,'form':form, 'weddingpackage':weddingpackage})
def services(request):
    venues = Venue.objects.filter(availability=True)
    catering = Catering.objects.all()
    stagedecoration = StageDecoration.objects.all()
    photography = Photography.objects.all()
    return render(request, 'service.html', {"venues": venues , 'catering':catering , 'photography':photography , 'stagedecoration':stagedecoration})

def book_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.venue = venue
            booking.save()
            messages.success(request, "Booking Successful!")
            return redirect('services')
    else:
        form = BookingForm()
    return render(request, 'book_venue.html', {'venue': venue, 'form': form})

def book_catering(request, catering_id):
    catering = get_object_or_404(Catering, id=catering_id)
    if request.method == 'POST':
        form = BookingFormCatering(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.catering = catering
            booking.save()
            messages.success(request, "Booking Successful!")
            return redirect('services')
    else:
        form = BookingFormCatering()
    return render(request, 'booking_catering.html', {'catering': catering, 'form': form})

def book_stage(request, stage_id):
    stage = get_object_or_404(StageDecoration, id=stage_id)
    if request.method == 'POST':
        form = BookingFormStageDecor(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.stageDecor = stage
            booking.save()
            messages.success(request, "Stage Decoration Booking Successful!")
            return redirect('services')
    else:
        form = BookingFormStageDecor()
    return render(request, 'book_stage.html', {'stage': stage, 'form': form})


def book_photography(request, photography_id):
    photography = get_object_or_404(Photography, id=photography_id)
    if request.method == 'POST':
        form = BookingFormPhotography(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.photography = photography
            booking.save()
            messages.success(request, "Photography Booking Successful!")
            return redirect('services')
    else:
        form = BookingFormPhotography()
    return render(request, 'book_photography.html', {'photography': photography, 'form': form})
def wedding_package(request):
    weddingpackage = WeddingPackage.objects.all()
    return render(request, 'wedding_package.html',{'weddingpackage':weddingpackage})

def book_package(request, package_id):
    weddingpackage = get_object_or_404(WeddingPackage, id=package_id)
    if request.method == 'POST':
        form = BookingFormWeddingPackage(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.weddingpackage = weddingpackage
            booking.save()
            messages.success(request, "Booking Successful!")
            return redirect('services')
    else:
        form = BookingFormWeddingPackage()
    return render(request, 'booking_package.html', {'weddingpackage': weddingpackage, 'form': form})

#contact form views
def contact_form(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_form')
    else:
        form = ContactForms()
    return render(request,'inc/contactpage.html',{'form':form})

def about(request):
    return render(request,'about.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')



