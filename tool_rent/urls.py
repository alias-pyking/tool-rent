from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ToolRent Admin'
admin.site.index_title = 'ToolRent Administration'
admin.site.site_title = 'ToolRent'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools/', include('tools.urls')),
    path('tools/', include('reviews.urls')),    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
