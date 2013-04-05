from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'equipeb.core.views.list_by_field', name='list_by_field'),
    url(r'^evento/(?P<pk>\d+)/$', 'equipeb.core.views.ver_evento', name='ver_evento'),
    url(r'^evento/(?P<pk>\d+)/subscription$', 'equipeb.core.views.subscription', name='subscription'),
    url(r'^palestra/(?P<pk>\d+)/$', 'equipeb.core.views.ver_palestra', name='ver_palestra'),
     # url(r'^equipeb/', include('equipeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
