from settings.models import Setting

def site_data(request):

    settings = Setting.objects.get(pk=1)
    
    return {
        'SITE_NAME': settings.name,
        'SITE_DESCRIPTION': settings.description,
        'SITE_KEYWORDS': settings.keywords,
        'MENU_COLOR': get_color(settings.menu_color),
        'NAVBAR_COLOR': get_color(settings.navbar_color),
        'FOOTER_DARK': get_footer_dark(settings.footer_dark)
    }

def get_color(n):
    if n == 1: 
        return 'gradient-45deg-indigo-blue'
    elif n == 2: 
        return 'gradient-45deg-purple-deep-orange'
    elif n == 3: 
        return 'gradient-45deg-light-blue-cyan'
    elif n == 4: 
        return 'gradient-45deg-purple-amber'
    elif n == 5: 
        return 'gradient-45deg-purple-deep-purple'
    elif n == 6: 
        return 'gradient-45deg-deep-orange-orange'
    elif n == 7: 
        return 'gradient-45deg-green-teal'
    elif n == 8: 
        return 'gradient-45deg-indigo-light-blue'
    elif n == 9: 
        return 'gradient-45deg-red-pink'
    elif n == 10: 
        return 'red'
    elif n == 11: 
        return 'purple'
    elif n == 12: 
        return 'pink'
    elif n == 13: 
        return 'deep_purple'
    elif n == 14: 
        return 'cyan'
    elif n == 15: 
        return 'teal'
    elif n == 16: 
        return 'light-blue'
    elif n == 17: 
        return 'amber darken-3'
    elif n == 18: 
        return 'brown darken-2'

def get_footer_dark(footer_dark):
    if footer_dark:
        return 'footer-dark'
    else:
        return 'footer-light'