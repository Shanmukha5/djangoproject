from django.conf.urls import include, url
from django.contrib import admin
from website import views as webviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/',(admin.site.urls)),
    url(r'^$', webviews.base),
    url(r'^about/',webviews.about),
    url(r'^contact/',webviews.contact),
    url(r'^services/',webviews.services),
    url(r'^products/',webviews.products),
    url(r'^blog/',webviews.blog),
    url(r'^hiring/',webviews.hiring),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


