from django.db import models
from icalendar import STATUS


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()


    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class Status(models.TextChoices):
    NEW = 'new', 'New'
    IN_PROGRESS = 'in-progress', 'In Progress'
    PENDING = 'pending', 'Pending'
    BLOCKED = 'blocked', 'Blocked'
    DONE = 'done', 'Done'

class Task(models.Model):
    title = models.CharField(max_length=100, unique_for_date="created_at")
    description = models.TextField()
    category = models.ManyToManyField(Book)
    status = models.CharField(max_length=15, choices=Status, default=Status.NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=Status, default=Status.NEW)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.task.title})"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name