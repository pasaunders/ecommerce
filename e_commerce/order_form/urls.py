from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rendering),
    url(r'^order', views.order),
    url(r'^checkout', views.checkout),
]
