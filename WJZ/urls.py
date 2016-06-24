from django.conf.urls import url
from django.contrib import admin
from APP import views as APP_views

urlpatterns = [
	url(r'^$', APP_views.index, name='index'),
	url(r'^handle/$', APP_views.handle, name='handle'),
	url(r'^ips/$', APP_views.get_ips, name='ips'),
	url(r'^admin/', admin.site.urls),
]
