from django.contrib import admin
from .models import Okopf, Okved, Region, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'update_time')
    search_fields = ['name']


admin.site.register(Okopf)
admin.site.register(Okved)
admin.site.register(Region)
admin.site.register(Company, CompanyAdmin)
