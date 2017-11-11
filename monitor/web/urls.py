from django.conf.urls import url

from monitor.web import views

app_name = "monitor"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user/$', views.user, name="user"),

]
