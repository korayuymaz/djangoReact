from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ToDo  # add this


class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'state')  # add this


# Register your models here.
admin.site.register(ToDo, TodoAdmin)  # add this
