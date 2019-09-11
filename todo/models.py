from django.db import models
from django.utils.html import format_html


class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        status_verb = ['todo', 'in progress', 'done']
        return f'title: "{self.title}" with status: "{status_verb[self.status]}"'

    def colored_str(self):
        return format_html(
            '<span style="color: #ee4a31;">{} with status: {}</span>', self.title, self.status
        )
