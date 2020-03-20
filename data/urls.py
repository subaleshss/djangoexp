from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('getdata',views.getdata,name='getdata'),
    path('view',views.viewdata,name='view')
]
