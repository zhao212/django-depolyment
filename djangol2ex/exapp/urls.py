from django.conf.urls import url
from exapp import views

urlpatterns= [
    url(r'^$',views.users,name='users'),
]
