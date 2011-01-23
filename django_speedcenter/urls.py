# -*- coding: utf-8 -*-

import os.path

from django.conf import settings
from django.conf.urls.defaults import patterns, include, handler404, handler500


urlpatterns = patterns('',
    (r'^ds-media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__), "media")}),
    (r'^sentry/', include('sentry.urls')),
)

urlpatterns += patterns('',
    (r'^', include('speedcenter.urls')),
)
