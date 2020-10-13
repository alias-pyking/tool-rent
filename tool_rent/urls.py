from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'ToolRent Admin'
admin.site.index_title = 'ToolRent Administration'
admin.site.site_title = 'ToolRent'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools/', include('tools.urls')),
    path('tools/', include('reviews.urls')),
    
]
