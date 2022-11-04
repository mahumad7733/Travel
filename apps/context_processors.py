from django.conf import settings

def cfg_assets_root(request):

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT }

def cfg_assets_root_website(request):

    return { 'ASSETS_ROOT_WEBSITE' : settings.ASSETS_ROOT_WEBSITE }

