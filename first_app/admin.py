from django.contrib import admin
from .models import Book, Category, SubTask, Task

# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(SubTask)
# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'status','created_at','deadline')
    list_filter = ('status',)
    search_fields = ('title','description',)
    ordering = ('-created_at',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status','created_at','deadline')
    list_filter = ('status',)
    search_fields = ('title','description',)
    ordering = ('-created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

