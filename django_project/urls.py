from django.conf.urls import patterns, include, url
from django.http import HttpRequest, HttpResponseRedirect
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', lambda r : HttpResponseRedirect('/home/')),

)
