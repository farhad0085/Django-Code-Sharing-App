from django.conf import settings


def sitename_tagline(request):
    
    context = {
        'SITENAME': settings.SITENAME,
        'TAGLINE': settings.TAGLINE
    }

    return context
