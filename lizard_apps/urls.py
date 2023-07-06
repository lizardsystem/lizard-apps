# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import url

from lizard_apps import views

urlpatterns = [
    url(r"^screens/(?P<slug>[\w-]+)\.json$", views.app_screen_view),
    url(r"^screens/(?P<slug>[\w-]+)\.js$", views.AppScreenView.as_view()),
]
