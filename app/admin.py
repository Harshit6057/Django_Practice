from django.contrib import admin
from .models import AppVariaty, AppReview, Store , AppCertificate



# Register your models here.
class AppReviewInline(admin.TabularInline):
    model = AppReview
    extra = 2
    
class AppVariatyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name', 'type')
    list_filter = ('type', 'date_added')
    inlines = [AppReviewInline]
    
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location'
                     )
    
class AppCertificateAdmin(admin.ModelAdmin):
    list_display = ('app', 'issued_by', 'issue_date', 'valid_until')
    search_fields = ('app__name', 'issued_by')
    
admin.site.register(AppVariaty, AppVariatyAdmin)
admin.site.register(Store, StoreAdmin )
admin.site.register(AppCertificate, AppCertificateAdmin)

