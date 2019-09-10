from django.contrib import admin

from todo.models import Task

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, AuthorAdmin)
