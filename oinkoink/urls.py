from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

from apps.core.views import frontpage, signup
from apps.feed.views import feed

from apps.feed.api import api_add_oink

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='core/logged_out.html'), name='logout'),
    path('password_reset/',
         views.PasswordResetView.as_view(template_name='core/password_reset.html'), name='password_reset'),

    path('feed/', feed, name='feed'),

    path('api/add_oink/', api_add_oink, name='api_add_oink'),

    path('admin/', admin.site.urls),
]
