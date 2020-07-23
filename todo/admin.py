from django.contrib import admin
from .models import Todo

# we cannot edit the created model thats why we have to make this custom class

class TodoAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)

# Register your models here.
admin.site.register(Todo, TodoAdmin)