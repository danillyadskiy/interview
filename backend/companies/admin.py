from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Okopf, Okved, Region, Company


class OkopfAdmin(admin.ModelAdmin):
    search_fields = ['name']


class OkvedAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CompanyAdmin(admin.ModelAdmin):
    # Список компаний
    list_display = ('pk', 'name', 'update_time')
    search_fields = ['name']

    # Форма изменения / добавления компании
    readonly_fields = ['create_time', 'update_time']
    autocomplete_fields = ['region', 'okopf', 'main_okved']
    filter_horizontal = ('okved',)
    formfield_overrides = {
        models.EmailField: {'widget': TextInput(attrs={'size': '50'})},
        models.URLField: {'widget': TextInput(attrs={'size': '50'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 1,
                                                     'cols': 50,
                                                     'style': 'resize:none;'})}
    }


admin.site.register(Okopf, OkopfAdmin)
admin.site.register(Okved, OkvedAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Company, CompanyAdmin)
