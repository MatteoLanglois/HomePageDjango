from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from home.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'icon', 'nom', 'type', 'description', 'link',
                    'visible')
    list_filter = ['titre', 'icon', 'nom', 'type', 'description', 'link',
                   'visible']
    search_fields = ['titre', 'icon', 'nom', 'type', 'description', 'link']
    empty_value_display = '-empty-'
    ordering = ['titre']


admin.site.register(Project, ProjectAdmin)
