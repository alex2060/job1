from django.urls import path
from . import views


urlpatterns = [
	path('add_user', views.home,name='home'),
    path('add_traid', views.home,name='add_traid'),
    path('post_reqest', views.post,name='post'),
    path('lbry_host', views.post,name='post'),
    path('cash', views.post,name='get_from_cash')
]


