
from django.urls import path, include

urlpatterns = [
    path('api/', include('luv_api.apps.api.products.urls', namespace='products')),
]
