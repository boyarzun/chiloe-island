from settings.models import Setting

def site_data(request):

    settings = Setting.objects.get(pk=1)
    
    
    return {
        'SITE_NAME': settings.name,
        'SITE_DESCRIPTION': settings.description,
        'SITE_KEYWORDS': settings.keywords
    }
