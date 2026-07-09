from django.contrib import admin
from .models import Book, Category, SubTask, Task

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(SubTask)
admin.site.register(Task)

