from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def services(request):
    return render(request, 'service-details.html')