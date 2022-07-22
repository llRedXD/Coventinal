from django.contrib import admin
from django.urls import include, path
from core.escola.urls import router as escola_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(escola_router.urls)),
    # path('api-auth/', include(escola_router.urls), name='rest_framework'),
]
