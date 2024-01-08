from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, \
    BlogDeleteView, ContactsPageView

app_name = CatalogConfig.name

urlpatterns = [
    # path('', index, name='index'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('blogs/', BlogListView.as_view(), name='list'),
    path('', ProductListView.as_view(), name='index'),
    path('view/<slug>/', BlogDetailView.as_view(), name='view'),
    path('edit/<slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
]
