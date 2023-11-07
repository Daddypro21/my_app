from django.contrib import admin

# Register your models here.
from first_app.models import Topic,WebPage,AccessRecord 

admin.site.register(Topic)
admin.site.register(WebPage) 
admin.site.register(AccessRecord)