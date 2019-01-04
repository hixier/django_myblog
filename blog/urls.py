# url

from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail-view'),
    path('blogs/bloggers/', views.AuthorListView.as_view(), name='bloggers'),
    path('blogs/bloggers/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('blogs/<int:pk>/create', views.comment_create, name='comment_create'),
]