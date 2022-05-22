from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('snippets.urls')),
    # path('quickstart/', include('REST_API.quickstart.urls')),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
