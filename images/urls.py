from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$', views.default, name='default'),
  url('^filter-usa$', views.filter_usa, name='filter-usa'),
  url('^filter-germany$', views.filter_germany, name='filter-germany'),
  url('^filter-italy$', views.filter_italy, name='filter-italy'),
  url('^filter-brazil$', views.filter_brazil, name='filter-brazil'),
  url('^filter-kenya$', views.filter_kenya, name='filter-kenya')
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)