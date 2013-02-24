from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from vReport.views import *
from api.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('api.urls')),

    # welcome page
    url(r'^$', welcome),

    # index page
    url(r'^index/', index),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Change password
    url(r'^pw/$', 'django.contrib.auth.views.password_change', {'template_name': 'vReport/pw.html', 'post_change_redirect':'/pw/success/'}),

    # Change password success
    url(r'^pw/success/', pw_success),

    #About
    url(r'^about/', about),

    #Add
    url(r'^add/', addReporter),

    url(r'^data/', getAggregateData),  

    # Login/logout
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'vReport/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    url(r'^approve/', approveReport),
    url(r'^deny/', denyReport),
)
