from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.sitemaps.views import sitemap

from .forms import ContactForm
from .sitemaps import StaticViewSitemap



def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def starter_page(request):
    return redirect('index')

def services(request):
    return render(request, 'service-details.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
        messages.error(request, 'Please correct the errors below and try again.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def testimonials(request):
    return render(request, 'testimonials.html')

def sitemap_view(request):
    response = sitemap(request, {'static': StaticViewSitemap})
    response.headers.pop('X-Robots-Tag', None)
    return response
