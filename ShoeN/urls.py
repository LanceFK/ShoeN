from django.urls import path
from . import views
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, CategoryListView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('category-list', CategoryListView, name='category-list'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
    path('hangman', views.index, name='hangman'),
    path('search_shoes', views.search_shoes, name='search_shoes'),    
    path('shoen_meta', views.shoen_meta, name='shoen_meta'),    


]