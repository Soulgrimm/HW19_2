from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, \
    BlogDeleteView, ContactsPageView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('view_product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='view_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blogs/', BlogListView.as_view(), name='list'),
    path('view/<slug>/', BlogDetailView.as_view(), name='view'),
    path('edit/<slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
]
