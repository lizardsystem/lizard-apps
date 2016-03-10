# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from lizard_apps.models import Screen


class AppScreenView(TemplateView):
    content_type = "application/javascript"
    template_name = "lizard_apps/script.js"

    def screen(self):
        return get_object_or_404(Screen, slug=self.kwargs['slug'])
