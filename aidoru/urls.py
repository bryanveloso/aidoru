from django.conf.urls import patterns, include, url
from django.contrib import admin

from modules.images.views import CountTheImagesView, RandomImageChoiceView


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', '', name='home'),

    # Endpoints (backwards-compatible with the Flask version).
    url(r'^count/$', CountTheImagesView.as_view(), name='count'),
    url(r'^random/$', RandomImageChoiceView.as_view(), name='random'),

    url(r'^admin/', include(admin.site.urls)),
)
