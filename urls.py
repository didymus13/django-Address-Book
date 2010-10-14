from django.conf.urls.defaults import *
from piston.resource import Resource

from handlers import ContactHandler, AddressHandler, TelephoneHandler, EmailHandler

contact_resource = Resource(handler=ContactHandler)
address_resource = Resource(handler=AddressHandler)
telephone_resource = Resource(handler=TelephoneHandler)
email_resource = Resource(handler=EmailHandler)

urlpatterns = patterns('',
                       url(r'^api/contacts/$', contact_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/$', contact_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/addresses/$', address_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/addresses/(?P<address>\d+)/$', address_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/telephone/$', telephone_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/telephone/(?P<address>\d+)/$', telephone_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/email/$', email_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/email/(?P<email>\d+)/$', email_resource),
                       )