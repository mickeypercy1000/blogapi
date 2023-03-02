"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('config/', include('config.urls'))
"""
from django.contrib import admin
from django.urls import path

from post.views import createAuthorView, createCategoryView, createPostView, deleteAuthorView, deleteCategoryView, deletePostView, detailAuthorView, detailPostView, listCategoryView, detailCategoryView, listPostView, updateCategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("categories", listCategoryView.as_view(), name='categories'),
    path("categories-create/", createCategoryView.as_view(), name='categories-create'),
    path("categories-detail/<str:pk>", detailCategoryView.as_view(), name='categories-detail'),
    path("categories-delete/<str:pk>", deleteCategoryView.as_view(), name='categories-delete'),
    path("categories-update/<str:pk>", updateCategoryView.as_view(), name='categories-update'),

    path("author", listCategoryView.as_view(), name='author'),
    path("author-create/", createAuthorView.as_view(), name='author-create'),
    path("author-detail/<str:pk>", detailAuthorView.as_view(), name='author-detail'),
    path("author-delete/<str:pk>", deleteAuthorView.as_view(), name='author-delete'),

    path("post", listPostView.as_view(), name='post'),
    path("post-create/", createPostView.as_view(), name='post-create'),
    path("post-detail/<str:pk>", detailPostView.as_view(), name='post-detail'),
    path("post-delete/<str:pk>", deletePostView.as_view(), name='post-delete')
]
