from django.shortcuts import render
from core.models import GeneralSetting

def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    slider_description = GeneralSetting.objects.get(name='slider_description').parameter

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'slider_description': slider_description,
    }

    return render(request, 'index.html', context=context)
def contact(request):
    return render(request, 'contact.html')
