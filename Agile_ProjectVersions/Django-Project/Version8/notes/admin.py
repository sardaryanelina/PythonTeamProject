from django.contrib import admin

from . import models

# Specifies which models can be displayed and modified via the admin interface. 

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Registers that that model we imported is attached to this admin model. 
admin.site.register(models.Note, NotesAdmin)