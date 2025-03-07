from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),

    # Esquema de API para documentación
    path('api/schema/', get_schema_view(title="API Schema", description="Esquema de API", version="1.0.0"),
         name='openapi-schema'),

    # Documentación con coreapi (si usas DRF 3.13.1)
    path('docs/', include_docs_urls(title='API Documentation')),

]
