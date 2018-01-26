from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.views.generic import TemplateView

import django_js_reverse.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('docs.urls')),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),

    # Django Rest Framework browsable API
    url(r'^api-browser/auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', TemplateView.as_view(template_name='exampleapp/itworks.html'), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
