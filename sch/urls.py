from django.urls import path
from sch import views


urlpatterns = [
    path('ls1/',views.list,name='ls1'),
    path('footer1',views.footer1,name='fo1'),
    path('subs1',views.subs1,name='sub1')
]
