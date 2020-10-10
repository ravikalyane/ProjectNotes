from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': ['name', 'age', 'location']}),
        ('Education', {'fields': ['email', 'course']})
    ]
    list_display = ('name', 'age','location', 'email', 'course')



admin.site.register(Profile, ProfileAdmin)









# ***************************************
class NoteAdmin(admin.ModelAdmin):
    list_display = 'title', 'date_created'


admin.site.register(Note, NoteAdmin)
admin.site.register(Hello)
admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
