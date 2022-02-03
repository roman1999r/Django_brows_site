from django.urls import path
from .views import *


urlpatterns = [
    path('logout/', user_logout, name="logout"),
    path('login/', user_login, name="login"),
    path('', index, name='home'),
    path('portfolio', portfolio, name='portfolio'),
    path('blog', Blog.as_view(), name='blog'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('adm', adm, name='adm'),
    path('blog/add-post/', CreatePost.as_view(), name='add_post'),
    path('blog/add-photo/', CreatePhoto.as_view(), name='add_photo'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('photo/<str:slug>/update/', PhotoUpdate.as_view(), name='photo_update'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('photo/<str:slug>/delete/', PhotoDelete.as_view(), name='photo_delete'),
    path('add_event', add_event, name='add_event'),
    path('about_us', about_us, name='about_us'),
    path('services', services, name='services'),
]