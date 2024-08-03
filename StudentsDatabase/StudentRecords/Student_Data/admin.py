from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('name' , 'email' , 'password')

# admin.site.register(User , UserAdmin)
# Register your models here.
