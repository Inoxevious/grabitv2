from django.contrib import admin
from .models import *
from mapwidgets.widgets import GooglePointFieldInlineWidget
from django.contrib.gis.db.models import PointField
class PackageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    fieldsets = [
        (None, {'fields': ['reference','qrCode','picture','location','available','valid']}),
    ]
    list_display = ('location','available','valid',)
    list_filter = ('available','valid',)
admin.site.register(User)
admin.site.register(Package,PackageAdmin)
