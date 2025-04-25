# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('core.urls')), 
#         path('django-admin/', admin.site.urls),  # Add this line
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),  # Your custom URLs
    path('django-admin/', admin.site.urls),  # Default admin (optional)
]