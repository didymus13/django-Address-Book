from django.contrib import admin
from models import *

class AddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Address, AddressAdmin)

class AddressInline(admin.TabularInline):
    model = Address

class TelephoneNumberAdmin(admin.ModelAdmin):
    pass
admin.site.register(TelephoneNumber, TelephoneNumberAdmin)

class TelephoneNumberInline(admin.TabularInline):
    model = TelephoneNumber

class EmailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Email, EmailAdmin)

class EmailInline(admin.TabularInline):
    model = Email

class ContactAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        TelephoneNumberInline,
        EmailInline,
    ]
admin.site.register(Contact, ContactAdmin)
