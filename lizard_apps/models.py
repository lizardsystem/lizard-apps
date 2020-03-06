# -*- coding: utf-8 -*-
# (c) Nelen & Schuurmans, see LICENSE.rst.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from lizard_apps import managers


class Application(models.Model):
    """An application in the sense of Google Apps.

    Well, `application` is perhaps a bit bombastic. It's just a bookmark
    that will be used to switch between our and third-party websites.

    Icon will be uploaded to MEDIA_ROOT/lizard_apps.
    """

    url = models.URLField()
    icon = models.ImageField(upload_to='lizard_apps/')
    name = models.CharField(
        db_index=True,
        help_text='Descriptive text for labeling the icon',
        max_length=64,
    )

    objects = managers.ApplicationManager()

    class Meta:
        ordering = ['name']
        unique_together = ('url', 'icon', 'name')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.url, self.icon.name, self.name)


class Screen(models.Model):
    """A collection of applications."""

    slug = models.SlugField(max_length=64, unique=True)
    applications = models.ManyToManyField(
        Application,
        related_name='screens',
        through='ApplicationScreen'
    )

    objects = managers.ScreenManager()

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.slug

    def natural_key(self):
        return (self.slug,)


class ApplicationScreen(models.Model):
    """Intermediary model for ordering applications on a screen.

    If no order if provided, ordering will be alphabetically.
    """

    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    order = models.IntegerField(blank=True, null=True)

    objects = managers.ApplicationScreenManager()

    class Meta:
        ordering = ['screen', 'order', 'application__name']
        unique_together = ('screen', 'application')

    def __str__(self):
        return self.application.url

    def natural_key(self):
        return (self.screen, self.application)
