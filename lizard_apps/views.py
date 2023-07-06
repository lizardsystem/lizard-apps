# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import get_list_or_404
from django.views.generic import TemplateView
from django.http import JsonResponse
from lizard_apps.models import Application


def get_apps_or_404(slug):
    return get_list_or_404(
        Application.objects.order_by("applicationscreen__order", "name"),
        screens__slug=slug,
    )


class AppScreenView(TemplateView):
    content_type = "application/javascript"
    template_name = "lizard_apps/script.js"

    def apps(self):
        return get_list_or_404(self.kwargs["slug"])


def app_screen_view(request, slug):
    return JsonResponse(
        [
            {
                "name": app.name,
                "url": app.url,
                "icon": request.build_absolute_uri(app.icon.url),
            }
            for app in get_apps_or_404(slug)
        ],
        safe=False,
    )
