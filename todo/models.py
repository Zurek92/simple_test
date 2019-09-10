from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    status = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __repr__(self):
        status_verb = ['todo', 'in progress', 'done']
        return f'title: "{self.title}" with status: "{status_verb[self.status]}"'
