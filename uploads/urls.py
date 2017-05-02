from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns

from uploads.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^uploads/core/templates/core/$', views.lotter_main_page, name='lotter_main_page'),
    url(r'^uploads/lotter_extract/$', views.lotter_extractor, name='lotter_extractor'),
    url(r'^uploads/predict_stock/$', views.predict_stock, name='predict_stock'),
    url(r'^uploads/model_desc/$', views.model_desc, name='model_desc'),
    url(r'^uploads/lotter_desc/$', views.lotter_desc, name='lotter_desc'),
    url(r'^admin/', admin.site.urls),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)

