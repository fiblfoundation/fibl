from django.contrib import admin

# Register your models here.
from . models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'skype_telegram', 'created', 'comments']
    list_editable = ['comments']
    list_filter = ['created',]
    search_fields = ['full_name', 'email', 'skype_telegram', 'created', 'comments']

    class Meta:
        model = Client

admin.site.register(Client, ClientAdmin)



