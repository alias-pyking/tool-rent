from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from users.views import VerifyEmailView

admin.site.site_header = 'ToolRent Admin'
admin.site.index_title = 'ToolRent Administration'
admin.site.site_title = 'ToolRent'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools/', include('tools.urls')),
    path('tools/', include('reviews.urls')),    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path('rest-auth/registration/account-confirm-email/(?P<key>.+)/', VerifyEmailView.as_view(),
            name='account_confirm_email'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
