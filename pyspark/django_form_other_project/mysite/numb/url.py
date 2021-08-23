from django.urls import path
from . import views


urlpatterns = [
	path('traider', views.traider,name='traider'),
    path('add_traid', views.add_traid,name='add_traid'),
    path('compleat_traid', views.compleat_traid,name='compleat_traid'),
    path('get_user_info', views.print_convertion,name='get_user_info'),
    path('convertion', views.print_convertion,name='convertion'),
    path('print_user', views.print_user,name='print_user'),
    path('doit', views.doit,name='doit')

]
#print_user

