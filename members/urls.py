from re import template
from django.urls import path
from .views import ShowProfilePageView, UserRegisterView, UserEditView, PasswordsChangeView, EditProfilePageView, ShowProfilePageView, CreateProfilePageView
from . import views 

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name= 'registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name= 'registration/change-password.html')),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('password_success', views.password_success, name= 'password_success'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('my_collection/', views.my_collection, name='my_collection'),

]