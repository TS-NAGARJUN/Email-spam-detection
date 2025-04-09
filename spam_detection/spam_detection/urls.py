from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spam.urls')),  # This includes the URLs from your spam app
]
