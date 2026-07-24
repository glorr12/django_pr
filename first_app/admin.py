from django.contrib import admin
from .models import Book, Category, SubTask, Task, Status

# admin.site.register(Book)
# admin.site.register(Category)
# admin.site.register(SubTask)
# admin.site.register(Task)
class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title','description','status','deadline',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = (SubTaskInline,)
    list_display = ( 'short_title', 'status','created_at','deadline')
    list_filter = ('status',)
    search_fields = ('title','description',)
    ordering = ('-created_at',)

    def short_title(self,obj):
        if len(obj.title) > 10:
            return f'{obj.title[:10]}...'
        return obj.title


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status','created_at','deadline')
    list_filter = ('status',)
    search_fields = ('title','description',)
    ordering = ('-created_at',)
    actions = ['mark_done']


@admin.action(description='Mark task as Done')
def mark_done(self, request, queryset):
    queryset.update(status=Status.DONE)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

