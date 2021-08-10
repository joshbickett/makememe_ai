from django.urls import path
# COMMENT: remember to add this line below
from . import views



urlpatterns = [
    path('', views.home, name='meme-home'),
    path('about/', views.about, name='meme-about'),
    path('blog/', views.blog, name='meme-blog'),
    path('technology/', views.technology, name='meme-technology'),
]