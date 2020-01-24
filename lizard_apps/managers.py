# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from django.db import models


class ApplicationManager(models.Manager):
    def get_by_natural_key(self, url, icon, name):
        return self.get(url=url, icon=icon, name=name)


class ScreenManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class ApplicationScreenManager(models.Manager):
    def get_by_natural_key(self, screen, application):
        return self.get(screen=screen, application=application)
