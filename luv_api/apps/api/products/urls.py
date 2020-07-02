from django.urls import path

from .views import BulkProductsPostView, ListProductsGetView

app_name = 'products'

urlpatterns = [
    path('products/bulk_insert', BulkProductsPostView.as_view()),
    path('products', ListProductsGetView.as_view() ),
]
