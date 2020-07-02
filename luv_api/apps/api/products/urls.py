from django.urls import path

from .views import BulkProductsPostView

app_name = 'products'

urlpatterns = [
    path('products/bulk_insert', BulkProductsPostView.as_view())
]
