from django.conf.urls.defaults import *
from piston.resource import Resource

from handlers import ContactHandler

contact_resource = Resource(handler=ContactHandler)

urlpatterns = patterns('',
                       url(r'^/api/contacts/$', contact_resource),
                       url(r'^/api/contacts/(?P<id>\d+/$', contact_resource),
                       )
