from django.contrib import admin

from todo.models import Task


class TaskAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'created', 'updated', 'colored_str')
    ordering = ('-updated',)

    def add_view(self, request):
        self.fields = ('title', 'status', 'content')
        self.readonly_fields = ()
        return super().add_view(request)

    def change_view(self, request, object_id):
        self.fields = (('title', 'status'), 'content', ('created', 'updated'))
        self.readonly_fields = ('title', 'content', 'created', 'updated')
        return super().change_view(request, object_id)

    def get_search_results(self, request, queryset, search_term):
        return Task.objects.all(), False


admin.site.register(Task, TaskAdmin)
