from django.contrib import admin

class costureiraweb(admin.ModelAdmin):
    view_on_site = False
    
admin.site.site_header = 'Costureiras WEB'
