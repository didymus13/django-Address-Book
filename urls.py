from django.conf.urls.defaults import *
from piston.resource import Resource

from handlers import *

contact_resource = Resource(handler=ContactHandler)
address_resource = Resource(handler=AddressHandler)
telephone_resource = Resource(handler=TelephoneHandler)
email_resource = Resource(handler=EmailHandler)
companyResource = Resource(handler=CompanyHandler)
companyTelephoneResource = Resource(handler=CompanyTelephoneHandler)
companyAddressResource = Resource(handler = CompanyAddressHandler )

urlpatterns = patterns('',
                       url(r'^api/contacts/$', contact_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/$', contact_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/addresses/$', address_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/addresses/(?P<address>\d+)/$', address_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/telephone-numbers/$', telephone_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/telephone-numbers/(?P<address>\d+)/$', telephone_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/email/$', email_resource),
                       url(r'^api/contacts/(?P<contact>\d+)/email/(?P<email>\d+)/$', email_resource),
                       
                       url(r'^api/company/$', companyResource),
                       url(r'^api/company/(?P<company_id>\d+)/$', companyResource),
                       url(r'^api/company/(?P<company_id>\d+)/telephone/$', companyTelephoneResource),
                       url(r'^api/company/(?P<company_id>\d+)/telephone/(?P<telephone_id>\d+)/$', companyTelephoneResource),
                       url(r'^api/company/(?P<company_id>\d+)/address/$', companyAddressResource),
                       url(r'^api/company/(?P<company_id>\d+)/address/(?P<address_id>\d+)/$', companyAddressResource),
                       )