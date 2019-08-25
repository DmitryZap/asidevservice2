from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Account, Project, ProjectFile


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    exclude = []
    list_filter = ['identificator']

    class Meta:
        model = Account


class FileAdmin(admin.TabularInline):
    model = ProjectFile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = []
    inlines = [FileAdmin]

    class Meta:
        model = Project
