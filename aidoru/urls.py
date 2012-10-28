from django.conf.urls import patterns, include, url
from django.contrib import admin

from modules.images.views import (BombIdolsView, CountTheImagesView,
    IndexView, RandomImageChoiceView)


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),

    # Endpoints (backwards-compatible with the Flask version).
    url(r'^count/$', CountTheImagesView.as_view(), name='count'),
    url(r'^random/$', RandomImageChoiceView.as_view(), name='random'),
    url(r'^bomb/$', BombIdolsView.as_view(), name='bomb'),

    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^selectable/', include('selectable.urls')),
)
