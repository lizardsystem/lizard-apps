# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.urls import re_path

from lizard_apps import views

urlpatterns = [
    re_path(r"^screens/(?P<slug>[\w-]+)\.json$", views.app_screen_view),
    re_path(r"^screens/(?P<slug>[\w-]+)\.js$", views.AppScreenView.as_view()),
]
