from django.contrib import admin
from models import *

"""
Contact Administrative Interface
"""
class ContactAddressInline(admin.TabularInline):
    model = ContactAddress

class ContactTelephoneInline(admin.TabularInline):
    model = ContactTelephone

class ContactEmailInline(admin.TabularInline):
    model = ContactEmail

class ContactAdmin(admin.ModelAdmin):
    inlines = [
        ContactAddressInline,
        ContactTelephoneInline,
        ContactEmailInline, ]
admin.site.register(Contact, ContactAdmin)

"""
Company Administrative Inteface
"""
class CompanyAddressInline(admin.TabularInline):
    model = CompanyAddress

class CompanyTelephoneInline(admin.TabularInline):
    model = CompanyTelephone
    
class CompanyEmailInline(admin.TabularInline):
    model = CompanyEmail
    
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyAddressInline,
        CompanyTelephoneInline,
        CompanyEmailInline, ]
admin.site.register(Company, CompanyAdmin)