from django.contrib import admin

# import models
from . import models

#new class NotesAdmin
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

#register model to allow CRUD in Admin Panel
admin.site.register(models.Notes, NotesAdmin)