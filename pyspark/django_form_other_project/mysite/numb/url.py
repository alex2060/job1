from django.urls import path
from . import views


urlpatterns = [
	path('number', views.home,name='home'),
    path('num_to_english', views.home,name='home'),
    path('post_reqest', views.post,name='post'),
    path('lbry_host', views.post,name='post'),
    path('cash', views.post,name='get_from_cash')
]


