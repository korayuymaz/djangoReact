from django.db import models

# Create your models here.


class ToDo(models.Model):
    STATES = [
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    state = models.CharField(
        max_length=15,
        choices=STATES,
        default='to_do',
    )

    def __str__(self):
        return self.title
